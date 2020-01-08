import re

from buildbot.process import logobserver
from buildbot.steps import Test

from buildbot.process.results import FAILURE
from buildbot.process.results import SUCCESS
from buildbot.process.results import WARNINGS

class GnuAutotestTestObserver(logobserver.LogLineObserver):

    def __init__(self):
        super().__init__()
        self.rc = SUCCESS
        self.failed = 0
        self.warnings = 0
        self.passed = 0
        self.complete = False

    failedRe = re.compile(r"\s+FAILED\s+")
    passedRe = re.compile(r"\s+ok\s+")
    skippedRe = re.compile(r"\s+skipped\s+")

    def outLineReceived(self, line):
        if self.failedRe.search(line):
            self.failed += 1
            self.rc = FAILURE
        if self.passedRe.search(line):
            self.passed += 1
        if self.skippedRe.search(line):
            self.warnings += 1


class GnuAutotestTest(Test):
    description = ["autotest"]
    command = ["make", "check", "-s"]
    total = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.observer = GnuAutotestTestObserver()
        self.addLogObserver('stdio', self.observer)

    def evaluateCommand(self, cmd):
        self.setTestResults(
            failed=self.observer.failed,
            passed=self.observer.passed,
            warnings=self.observer.warnings)

        rc = self.observer.rc
        if rc == SUCCESS and self.observer.warnings:
            rc = WARNINGS
        return rc

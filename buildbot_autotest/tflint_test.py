from buildbot.process import logobserver

from buildbot.steps.shell import Test
from buildbot.process.results import FAILURE
from buildbot.process.results import SUCCESS
from buildbot.process.results import WARNINGS

# rename -> tflint test
class JsonTestObserver(logobserver.LogObserver):

    def __init__(self):
        super().__init__()
        self.rc = SUCCESS
        self.failed = 0
        self.warnings = 0
        self.passed = 0
        self.complete = False

    def outLineReceived(self, line):
        data = json.load(line)
        if len(data['errors']):
            self.failed += len(data['errors'])
            self.rc = FAILURE
        elif len(data['issues']):
            self.warnings += len(data['issues'])
            self.rc = WARNINGS
        else:
            self.rc = SUCCESS
       

# rename tflint test
class TflintTest(Test):
    name = "tflint"
    description = ["running", "tflint"]
    descriptionDone = ["tfling"]

    command = ["tflint", "--format", "json"]

    def __init__(self, *args, **kwargs):
        self.command += [kwargs['case']]
        del kwargs['case']
        super().__init__(*args, **kwargs)
        self.observer = JsonTestObserver()
        self.addLogObserver('stdio', self.observer)

    def evaluateCommand(self, cmd):
        self.setTestResults(
            failed=self.observer.failed,
            passed=self.observer.passed,
            warnings=self.observer.warnings)

        rc = self.observer.rc

        return rc

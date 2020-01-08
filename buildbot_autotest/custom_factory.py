from buildbot.process.factory import BuildFactory
from buildbot.steps.shell import ShellCommand
from buildbot.steps.shell import Configure

from buildbot_autotest.gnu_autotest_test import GnuAutotestTest

class TerraformExamples(BuildFactory):
    def __init__(self, source):
        super().__init__([source])

        # autoreconf
        reconf = ["autoreconf","-si"]
        self.addStep(ShellCommand(name="autoreconf", command=reconf))

        # ./configure
        configure = "./configure"
        self.addStep(Configure(command=configure))

        # make check -s
        self.addStep(GnuAutotestTest())

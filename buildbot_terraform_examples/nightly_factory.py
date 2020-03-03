from buildbot.process.factory import BuildFactory
from buildbot.steps.shell import ShellCommand
from buildbot.steps.shell import Configure
from buildbot.steps.transfer import StringDownload

from buildbot_terraform_examples.gnu_autotest_test import GnuAutotestTest

class NightlyFactory(BuildFactory):
    def __init__(self, source, config):
        super().__init__([source])

        # create local tfvars config
        self.addStep(StringDownload(config, workerdest="terraform.tfvars"))
        # autoreconf
        reconf = ["autoreconf","-si"]
        self.addStep(ShellCommand(name="autoreconf", command=reconf))

        # ./configure
        configure = "./configure"
        self.addStep(Configure(command=configure))

        # make init
        init = ["make", "init"]
        self.addStep(ShellCommand(name="init", command=init))

        # make check -s
        self.addStep(GnuAutotestTest())

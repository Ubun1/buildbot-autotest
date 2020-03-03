from buildbot.process.factory import BuildFactory
from buildbot.plugins import util
from buildbot.steps.python import Sphinx
from buildbot.steps.transfer import StringDownload
from buildbot.steps.shell import ShellCommand

class PRFactory(BuildFactory):

    def __init__(self, source, config, sphinx_conf):
        super().__init__([source])
        
        # create _static dir
        self.addStep(ShellCommand(command=['mkdir', './cases/_static']))

        # lint rst
        self.addStep(StringDownload(sphinx_conf, workerdest="./cases/conf.py"))
        self.addStep(Sphinx(sphinx_builddir='build', 
            sphinx_sourcedir='cases',
            strict_warnings=True,
            ))

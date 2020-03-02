from buildbot.process.factory import BuildFactory
from buildbot.plugins import util
from buildbot.steps.python import Sphinx
from buildbot.steps.transfer import StringDownload

from buildbot_autotest.tflint_test import TflintTest

class PRFactory(BuildFactory):
    def __init__(self, source, config):
        super().__init__([source])
        # lint commit messages
        # ?

        # create local tfvars config
        self.addStep(StringDownload(config, workerdest="terraform.tfvars"))

        # lint rst
        basepath = util.Property('builddir')
        self.addStep(Sphinx(sphinx_builddir='{0}/build'.format(basepath), sphinx_sourcedir='{0}/cases'.format(basepath)))

        # lint .tf
        self.addStep(TflintTest())

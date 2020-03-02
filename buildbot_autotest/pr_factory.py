import os
import glob

from buildbot.process.factory import BuildFactory
from buildbot.plugins import util
from buildbot.steps.python import Sphinx
from buildbot.steps.transfer import StringDownload

from buildbot_autotest.tflint_test import TflintTest

class PRFactory(BuildFactory):

    _cases = [
        "./cases/aws_ami",
        "./cases/aws_ami_from_instance",
        "./cases/aws_ami_launch_permission",
        "./cases/aws_customer_gateway",
        "./cases/aws_default_network_acl",
        "./cases/aws_default_route_table",
        "./cases/aws_default_security_group",
        "./cases/aws_default_vpc",
        "./cases/aws_default_vpc_dhcp_options",
        "./cases/aws_ebs_snapshot",
        "./cases/aws_ebs_volume",
        "./cases/aws_eip",
        "./cases/aws_eip_association",
        "./cases/aws_instance",
        "./cases/aws_key_pair",
        "./cases/aws_network_acl",
        "./cases/aws_network_acl_rule",
        "./cases/aws_network_interface",
        "./cases/aws_placement_group",
        "./cases/aws_route",
        "./cases/aws_route_table",
        "./cases/aws_route_table_association",
        "./cases/aws_s3_bucket",
        "./cases/aws_security_group",
        "./cases/aws_security_group_rule",
        "./cases/aws_snapshot_create_volume_permission",
        "./cases/aws_subnet",
        "./cases/aws_volume_attachment",
        "./cases/aws_vpc",
        "./cases/aws_vpc_dhcp_options",
        "./cases/aws_vpc_dhcp_options_association",
    ]

    def __init__(self, source, config, sphinx_conf):
        super().__init__([source])
        # lint commit messages
        # ?

        # create local tfvars config
        self.addStep(StringDownload(config, workerdest="terraform.tfvars"))

        # lint rst
        self.addStep(StringDownload(sphinx_conf, workerdest="./cases/conf.py"))
        self.addStep(Sphinx(sphinx_builddir='build', sphinx_sourcedir='cases'))

        # lint .tf
        for case in self._cases:
            self.addStep(TflintTest(case=case))

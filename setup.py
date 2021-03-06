#!/usr/bin/env python

from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

VERSION = "0.0.1"

setup(name='buildbot-terraform-examples',
      version=VERSION,
      description='buildbot plugin for integration with autotest.',
      author='Nikita Kretov',
      author_email='kretov995@gmail.com',
      url='https://github.com/Ubun1/buildbot-autotest',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=['buildbot_terraform_examples'],
      requires=[
          "buildbot (>=2.0.0)"
      ],
      entry_points={
          "buildbot.util": [
              "NightlyFactory = buildbot_terraform_examples.nightly_factory:NightlyFactory",
              "PRFactory = buildbot_terraform_examples.pr_factory:PRFactory",
          ],
      },
      classifiers=[
          "Development Status :: 3 - Alpha"
          "Environment :: Plugins",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Operating System :: Linux",
          "Topic :: Software Development :: Build Tools",
      ]
      )

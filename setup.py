#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
  name='CPS xml to json',
  version='1.0',
  description='Convert xml feed to json',
  author='Jan Kurs',
  packages=find_packages(),
  include_package_data=True,
  install_requires=[
    'flask',
  ]
)
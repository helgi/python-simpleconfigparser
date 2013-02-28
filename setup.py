#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

PKG='SimpleConfigParser'
VERSION='0.1.0'

setup(name=PKG,
      version=VERSION,
      description="Simplified ConfigParser",
      author="Helgi Þorbjörnsson",
      author_email="helgi@php.net",
      url="http://github.com/helgi/python-simpleconfigparser",
      packages = find_packages(),
      install_requires = [],
      license = "MIT License",
      keywords="ConfiParser,ini",
      zip_safe = True,
      test_suite="tests",
      tests_require=['coverage', 'mock'])

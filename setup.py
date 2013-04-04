#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from os.path import join, dirname


def read(fname):
    return open(join(dirname(__file__), fname)).read()

PKG = 'SimpleConfigParser'
VERSION = '0.1.0'

setup(
    name=PKG,
    version=VERSION,
    description="Simplifies and enchances functionalities in Python's ConfigParser",
    long_description=read('README.rst'),
    author="Helgi Þorbjörnsson",
    author_email="helgi@php.net",
    url="http://github.com/helgi/python-simpleconfigparser",
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    platforms=['any'],
    install_requires=[],
    license="MIT License",
    keywords="ConfiParser,ini",
    zip_safe=True,
    test_suite="tests",
    tests_require=['setuptools'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ]
)

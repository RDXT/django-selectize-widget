#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import codecs
import os

from setuptools import setup, find_packages

from selectize_widget import VERSION


def read(file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    return codecs.open(file_path, encoding='utf-8').read()


PACKAGE = "selectize_widget"
NAME = "django-selectize-widget"
DESCRIPTION = "Selectize widget for Django"
AUTHOR = "Scott Adams"
AUTHOR_EMAIL = "scott@rdxt.com"
URL = "https://github.com/RDXT/django-selectize-widget"
VERSION = '.'.join(map(str, VERSION)),

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=read("README.md"),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="LICENSE.txt",
    url=URL,
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Framework :: Django",
    ],
)

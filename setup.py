#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages
import deuces
 
setup(
    name='deuces',
    version=deuces.__version__,
    packages=find_packages(),
    author="Will Drevo",
    description="Poker hand evaluator",
    long_description=open('README.md').read(),
    include_package_data=True,
    url='https://github.com/worldveil/deuces',
    license="WTFPL",
 
)
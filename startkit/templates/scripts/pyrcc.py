#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from setuptools import find_packages

print('=============================PYRCC====================================')

for package in find_packages(exclude=['tests']):
    for root, dirs, files in os.walk(package):
        for name in filter(lambda x: x.endswith('.qrc'), files):
            name = os.path.abspath(os.path.join(root, name))[:-4]
            os.system('pyrcc5 -o ' + name + '_rc.py ' + name + '.qrc')

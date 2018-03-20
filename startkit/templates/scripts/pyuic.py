#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from setuptools import find_packages

print('=============================PYUIC====================================')

for package in find_packages(exclude=['tests']):
    for root, dirs, files in os.walk(package):
        for name in filter(lambda x: x.endswith('.ui'), files):
            name = os.path.abspath(os.path.join(root, name))[:-3]
            os.system('pyuic5 -o ' + name + '.py ' + name + '.ui --from-imports')

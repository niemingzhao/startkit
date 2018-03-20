#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

config = {
    'name': 'startkit',  # Required
    'version': '1.2.0',  # Required
    'description': 'A skeleton generator for python projects.',  # Required
    'long_description': long_description,
    'long_description_content_type': 'text/markdown',
    'author': 'Nie Mingzhao',
    'author_email': '1432440963@qq.com',
    'url': 'https://github.com/niemingzhao/startkit',
    'download_url': 'https://github.com/niemingzhao/startkit/archive/master.zip',
    'keywords': 'skeleton project development',
    'platforms': 'any',
    'license': 'MIT',
    'classifiers': [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6'
    ],

    'packages': find_packages(exclude=['tests']),  # Required
    'include_package_data': True,
    'python_requires': '~=3.6',
    'install_requires': [],

    'entry_points': {
        'console_scripts': [
            'startkit=startkit.__main__:main'
        ]
    }
}

setup(**config)

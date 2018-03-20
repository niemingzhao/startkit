#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

config = {
    'name': '{{ project }}',  # Required
    'version': '{{ version }}',  # Required
    'description': '{{ description }}',  # Required
    'long_description': long_description,
    'long_description_content_type': 'text/markdown',
    'author': '{{ author }}',
    'author_email': '{{ email }}',
    'url': '',
    'download_url': '',
    'keywords': '',
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
    'install_requires': ['PyQt5'],

    'entry_points': {
        'console_scripts': [
            '{{ project }}={{ package }}.__main__:main'
        ]
    }
}

setup(**config)

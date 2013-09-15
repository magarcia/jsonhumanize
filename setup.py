#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='jsonhumanize',
    version='0.1.0',
    description='Convert JSON to human readable HTML',
    long_description=readme + '\n\n' + history,
    author='Martin Garcia',
    author_email='newluxfero@gmail.com',
    url='https://github.com/magarcia/jsonhumanize',
    packages=[
        'jsonhumanize',
    ],
    package_dir={'jsonhumanize': 'jsonhumanize'},
    entry_points = {
        'console_scripts': [
            'json-humanize = jsonhumanize:main'
        ]
    },
    include_package_data=True,
    install_requires=[
    ],
    license="MIT",
    zip_safe=False,
    keywords='jsonhumanize',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)
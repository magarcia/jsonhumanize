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

readme = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                      'readme.rst')
readme = open(readme).read()

history = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                       'HISTORY.rst')
history = open(history).read().replace('.. :changelog:', '')

requirements = [
    'Sphinx==1.2b1',
    'coverage==3.6',
    'flake8==2.0',
    'lxml==3.2.3',
    'pep8==1.4.6',
    'pyflakes==0.7.3',
    'tox==1.6.1',
    'nose==1.3.0'
]

if sys.version_info[0] == 2 and sys.version_info[1] < 7:
    requirements.append('simplejson==3.3.0')
    requirements.append('ordereddict==1.1')

setup(
    name='jsonhumanize',
    version='0.1.1',
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
            'json-humanize = jsonhumanize:main']
    },
    include_package_data=True,
    install_requires=requirements,
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

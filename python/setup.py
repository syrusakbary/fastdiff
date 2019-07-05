#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # wasmer, if we are in Linux x86_64
    'wasmer; python_version>"3.2" and platform_machine=="x86_64" and sys_platform=="linux"',
    # wasmer, if we are in macOS x86_64
    'wasmer; python_version>"3.2" and platform_machine=="x86_64" and sys_platform=="darwin"'
]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Syrus Akbary",
    author_email='me@syrusakbary.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="A fast native implementation of diff algorithm with a pure python fallback",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='fastdiff',
    name='fastdiff',
    packages=find_packages(include=['fastdiff']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/syrusakbary/fastdiff',
    version='0.1.2',
    zip_safe=False,
)

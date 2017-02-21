#!/usr/bin/env python3

from setuptools import find_packages, setup


with open('requirements.txt') as requirements:
    required = requirements.read().splitlines()

with open('README.rst') as readme:
    long_description = readme.read()


setup(
    name='dollars',
    version='0.1',
    description='Converts everything to dollars using up to date rates for '
                'free',
    long_description=long_description,
    url='http://github.com/aerupt/dollars',
    author='Lasse Schuirmann',
    author_email='lasse.schuirmann@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=required,
)

# -*- coding: utf-8
import os

from setuptools import find_packages, setup

PACKAGE_VERSION = '0.1.0'
README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='all-my-saints-website',
    version=PACKAGE_VERSION,
    packages=find_packages(),
    include_package_data=True,
    description="Optimics fun teambuilding game",
    long_description=README,
    url='https://github.com/just-paja/all-my-saints',
    author='Pavel Žák',
    author_email='pavel@zak.global',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

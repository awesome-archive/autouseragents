# -*- coding: utf-8 -*-
# @Author: broono
# @Date:   2016-04-10
# @Last Modified by:   broono
# @Last Modified time: 2016-04-12


import codecs
import os

try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup, find_packages


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


NAME = "autouseragents"
PACKAGES = find_packages()
REQUIREMENTS = ["requests", "bs4"]
DESCRIPTION = "A simple script to easily generate browser/robot User-Agent."
LONG_DESCRIPTION = read("README.rst")
KEYWORDS = "python user-agent generator faker"
AUTHOR = "Broono"
AUTHOR_EMAIL = "tosven.broono@gmail.com"
URL = "https://github.com/brunobell/python-auto-user-agents"
VERSION = "0.5"
LICENSE = "MIT"

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords=KEYWORDS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=True,
    install_requires=REQUIREMENTS,
)

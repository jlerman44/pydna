#!/usr/bin/env python
# -*- coding: utf-8 -*-

import versioneer

# Read author etc. from __init__.py
for line in open('pydna/__init__.py', encoding="utf-8"):
    if line.startswith('__') and not line.startswith('__version') and not line.startswith('__long'):
        exec(line.strip())

from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

try:
    from pypandoc import convert_file
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    with open("README.md", encoding="utf-8") as f:
        long_description = f.read()
else:
    long_description = "\n"+convert_file("README.md", 'rst')                                    

setup(  name            = 'pydna',
        version=versioneer.get_version()[:5],
        cmdclass=versioneer.get_cmdclass(),
        author          = __author__,
        author_email    = __email__,
        zip_safe = False,
        packages=['pydna'],
        url='http://pypi.python.org/pypi/pydna/',
        license='LICENSE.txt',
        description='''Contains classes and code for representing double
                     stranded DNA and functions for simulating homologous
                     recombination between DNA molecules.''',
        long_description=long_description,
        install_requires = ["appdirs", "biopython", "prettytable",  "networkx", "pyparsing", "requests"],
        keywords = "bioinformatics",
        classifiers = ['Development Status :: 4 - Beta',
                       'Environment :: Console',
                       'Intended Audience :: Education',
                       'Intended Audience :: Developers',
                       'Intended Audience :: Science/Research',
                       'License :: OSI Approved :: BSD License',
                       'Operating System :: OS Independent',
                       'Programming Language :: Python :: 3.5',
                       'Programming Language :: Python :: 3.6',
                       'Topic :: Education',
                       'Topic :: Scientific/Engineering :: Bio-Informatics',])

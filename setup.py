#!/usr/bin/env python

from setuptools import setup

setup(name="vi_refactor",
    version="0.0.3",
    description="CLI tool for refactoring your codebase with vi/m.",
    author="Eric Falkenberg",
    author_email="exf4789@rit.edu",
    url="https://ericfalkenberg.github.io/vi_refactor/",
    py_modules=['vi_refactor'],
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        vi_refactor=vi_refactor:cli
    ''',
)  

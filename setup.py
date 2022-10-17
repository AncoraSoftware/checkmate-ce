# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(name='checkmate',
version='0.2.0',
author=u'Andreas Dewes - QuantifiedCode UG (haftungsbeschränkt)',
author_email = 'andreas@quantifiedcode.com',
license = 'MIT',
install_requires = [
"blitzdb3@https://github.com/marcinguy/blitzdb3-ce@master#egg=blitzdb3",
'pylint',
'pyflakes',
'pep8',
'six',
'chardet',
'pyyaml',
'sqlalchemy'
],
entry_points = {
        'console_scripts': [
               'checkmate = checkmate.scripts.manage:main',
        ],
    },
url='https://github.com/marcinguy/checkmate-ce',
packages=find_packages(),
zip_safe = False,
description='A meta-code checker written in Python.',
long_description="""
Checkmate is a cross-language (meta-)tool for static code analysis, written in Python.
Unlike other tools, it provides a global overview of the code quality in a project and aims
to provide clear, actionable insights to the user.

Documentation
=============

The documentation can be found `here <https://github.com/marcinguy/checkmate-ce>`.

Source Code
===========

The source code can be found on `Github <https://github.com/marcinguy/checkmate-ce>`.

Changelog
=========

* 0.2.0: Beta-release
"""
)

#! /usr/bin/env python
#
# This file is part of TournamentMaster.
# Copyright (C) 2017  Simon Chen
#
# TournamentMaster is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TournamentMaster is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with TournamentMaster. If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup

setup(
    name='TournamentMaster',
    version='3.0.0',
    description='CLI for running tournaments between chess engines',
    url='https://github.com/Khold6458/TournamentMaster',
    author='Simon Chen',
    author_email='khold6458@gmail.com',
    license='GPLv3',
    keywords='chess engine tournament',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Games/Entertainment :: Board Games',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    py_modules=['tm'],
    install_requires=[
        'click',
        'python-chess'
    ],
    entry_points="""
        [console_scripts]
        tm=tm:cli
    """
)

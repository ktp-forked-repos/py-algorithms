#!/usr/bin/env python
import sys

from setuptools import find_packages
from setuptools import setup

import versioneer

if sys.version_info < (3, 5, 0):
    raise RuntimeError("Py Algorithms library requires Python 3.5.0+")

setup(
    name="py-algorithms",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Roman Lishtaba",
    author_email="roman@lishtaba.com",
    keywords=["algorithms", "python"],
    description="",
    long_description="",
    license="GPL v3",
    scripts=[],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
    ],
    install_requires=[
        'packaging>=16',
        'PyYAML>=3,<4',
        'six>=1,<2',
    ],
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
)

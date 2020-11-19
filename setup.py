#!/usr/bin/env python
import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 8):
    raise Exception('Only Python 3.8+ is supported')

setup(name='moonshine',
      version='0.1',
      description="Python module finder/loader from github, like in golang",
      author='Lewi Uberg',
      author_email='lewiuberg@gmail.com',
      url='https://github.com/lewiuberg/moonshine',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples',
                                      'tests', 'release']),
      include_package_data=True,
      zip_safe=False)

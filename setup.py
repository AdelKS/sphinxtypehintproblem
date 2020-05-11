#!/usr/bin/env python3

from setuptools import setup
from Cython.Build import cythonize

def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='foo',     
      ext_modules = cythonize("foo/foomodule.pyx", language_level=3),   
      packages=['foo'],
      include_package_data=True,
      zip_safe=False)
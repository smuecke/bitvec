#!/usr/bin/env python

from distutils.core import setup

setup(
        name='bitvec',
        version='0.1',
        description='Toolbox for binary vectors',
        author='Sascha Muecke',
        author_email='sascha.muecke@tu-dortmund.de',
        packages=['bitvec'],
        requires=['numpy']
)

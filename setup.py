#!/usr/bin/env python

from distutils.core import setup

setup(
        name='bitvec',
        packages=['bitvec'],
        version='0.1',
        description='Toolbox for binary vectors',
        author='Sascha Muecke',
        author_email='sascha.muecke@tu-dortmund.de',
        url='https://github.com/smuecke/bitvec',
        requires=['numpy']
)

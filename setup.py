#!/usr/bin/env python

import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(
        name='bitvec',
        packages=['bitvec'],
        version='0.1',
        description='Toolbox for binary vectors',
        long_description=long_description,
        long_description_content_type='text/markdown',
        author='Sascha Muecke',
        author_email='sascha.muecke@tu-dortmund.de',
        url='https://github.com/smuecke/bitvec',
        requires=['numpy']
)

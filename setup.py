#!/usr/bin/python3
import setuptools
from distutils.core import setup
from os import path
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='spyse.py',
      version='0.13.3.9',
      description='API wrapper & client for spyse.com',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Dominik Penner',
      author_email='zer0pwn@riseup.net',
      keywords='spyse spyse.py spyse.com zeropwn zer0pwn recon',
      url='https://github.com/zeropwn/spyse.py',
      packages=['spyse'],
      scripts=['bin/spyse'],
      install_requires=['requests']
     )

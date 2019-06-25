#!/usr/bin/python3

from distutils.core import setup

setup(name='spyse.py',
      version='1.0',
      description='API wrapper & client for spyse.com',
      author='Dominik Penner',
      author_email='zer0pwn@riseup.net',
      url='https://www.twitter.com/zer0pwn',
      packages=['spyse'],
      scripts=['bin/spyse']
     )

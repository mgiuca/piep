#!/usr/bin/env python

## NOTE: ##
## this setup.py was generated by zero2pypi:
## http://gfxmonk.net/dist/0install/zero2pypi.xml

from setuptools import *
setup(
	packages = find_packages(exclude=['test', 'test.*']),
	entry_points={'console_scripts': ['piep=piep.main:main']},
	name='piep',
	url='http://gfxmonk.net/dist/0install/piep.xml',
	install_requires=['setuptools', 'python<3', 'pygments'],
	version='0.6.2',
	long_description='\n**Note**: This package has been built automatically by\n`zero2pypi <http://gfxmonk.net/dist/0install/zero2pypi.xml>`_.\nIf possible, you should use the zero-install feed instead:\nhttp://gfxmonk.net/dist/0install/piep.xml\n\n----------------\n\npiep\n====\n\nBringing the power of python to stream editing\n----------------------------------------------\n\n| Zero install feed:\n| http://gfxmonk.net/dist/0install/piep.xml\n|\n| Online documentation:\n| http://gfxmonk.net/dist/doc/piep/\n|\n| Source Code / Issues:\n| https://github.com/gfxmonk/piep/\n|\n| Cheese shop entry:\n| http://pypi.python.org/pypi/piep\n',
	description="unix-style stream manipulation with python's syntax",
)

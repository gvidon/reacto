# !/usr/bin/env python
from setuptools import find_packages, setup

setup(
	author='Artem Rudenko',
	author_email='gvidon@ottofeller.com',
	description='Set of commands to maintain react apps and components',

	entry_points={
  	'console_scripts': [
			'reacto = reacto.main:cli',
		],
	},

	install_requires=['click', 'cookiecutter',],
	keywords=['react', 'js', 'tools', ],
	name='reacto',
	packages=['reacto',],
	version='0.1.0',
	url='https://github.com/gvidon/reacto',
)

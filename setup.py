# !/usr/bin/env python
from setuptools import find_packages, setup


setup(
	name='reacto',
	packages=find_packages(),
	version='0.1.0',
	description='Set of commands to maintain react apps and components',
	author='Artem Rudenko',
	author_email='gvidon@ottofeller.com',
	url='https://github.com/gvidon/reacto',
	keywords=['react', 'js', 'tools', ],

	entry_points={
  	'console_scripts': [
			'reacto = reacto.main:cli',
		],
	},
)

# !/usr/bin/env python
from setuptools import find_packages, setup
from reacto import __version__ as reacto_version


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
	version=reacto_version,
	url='https://github.com/gvidon/reacto',
)

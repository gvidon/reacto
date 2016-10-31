import click
from cookiecutter.main import cookiecutter
import os
import re


@click.command('start-component', short_help='start new component')
@click.argument('path')
@click.option('--actions/--no-actions', default=False, help='Add actions.js with empty actions set')
@click.option('--flow/--no-flow', default=True, help='Create component in a Flow way, it means add type checking')
@click.option('--reducers/--no-reducers', default=False, help='Add reducers.js with empty reducers set')
@click.option('--routes/--no-routes', default=False, help='Add routes.js with empty routes set')
@click.option('--route-path', default='', help='Add reducers.js with empty reducers set')
def start_component(path, actions, flow, reducers, routes, route_path):
	'''
	Start new component

	PATH is the component name or file system path. In the first case component will be created in current dir.
	'''

	# Get directory path where to put new component
	dir = re.sub('[\w\d]+/?$', '.', path)

	# Component name may be passed as fs path
	name = re.sub('/$', '', path).split('/').pop()

	cookiecutter(
		'gh:gvidon/cookiecutter-reacto-component',

		extra_context={
			'add_flow'      : flow,
			'component_name': name,
			'has_actions'   : actions,
			'has_reducers'  : reducers,
			'has_routes'    : routes,
			'route_path'    : route_path,
		},

		no_input=True,
		output_dir=dir,
	)

	# There is no way for cookiecutter <= 1.4.0 hooks to get to the generated project dir
	if not actions:
		os.remove('%s/%s/actions.js' % (dir, name))

	if not reducers:
		os.remove('%s/%s/reducers.js' % (dir, name))

	if not routes:
		os.remove('%s/%s/routes.js' % (dir, name))

	click.secho('Created new component %s in %s' % (name, dir), fg='green')


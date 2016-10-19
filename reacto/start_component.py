import click
from cookiecutter.main import cookiecutter
import os
import re


@click.command('start-component')
@click.argument('path')
@click.option('--actions/--no-actions', default=False)
@click.option('--flow/--no-flow', default=True)
@click.option('--reducers/--no-reducers', default=False)
@click.option('--routes/--no-routes', default=False)
@click.option('--route-path', default='')
def start_component(path, actions, flow, reducers, routes, route_path):

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


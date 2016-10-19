#!/usr/bin/env python
import click
from start_component import start_component


@click.group()
def cli():
	pass

cli.add_command(start_component)

# coding: utf-8

import click


@click.command(short_help="This is a short docstring.")
@click.option("--param", help="Param description.")
def addon_command(param):
    """This is a long docstring for this addon command.
    """
    print "Testing a deployvcmd addon command..."
    print "You passed: {param}".format(param=param)

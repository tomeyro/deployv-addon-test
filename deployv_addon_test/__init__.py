# coding: utf-8

import commands


def get_commands():
    return [
        commands.addon_command,
        "this raises a warning",
    ]


def cli():
    print "Run this addon from 'depoyvcmd' command."

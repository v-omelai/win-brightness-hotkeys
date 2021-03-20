import shlex
import subprocess

import click


@click.command()
@click.option('--command', required=True)
def run_in_background(command):
    """
    :param command: Command to be executed
    :type command: str
    """
    print(f'Log: {__file__} -> {command}')
    subprocess.Popen(shlex.split(command),
                     shell=True,
                     stdin=subprocess.DEVNULL,
                     stdout=subprocess.DEVNULL,
                     stderr=subprocess.DEVNULL)


if __name__ == '__main__':
    run_in_background()

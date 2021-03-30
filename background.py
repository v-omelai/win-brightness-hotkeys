import shlex
import subprocess

import click


@click.command()
@click.option('--command', required=True, help='Command to be executed in the background')
def cli(command: str):
    """
    For more reference see:

    CLI: https://click.palletsprojects.com/en/7.x/options/
    """
    subprocess.Popen(shlex.split(command),
                     shell=True,
                     stdin=subprocess.DEVNULL,
                     stdout=subprocess.DEVNULL,
                     stderr=subprocess.DEVNULL)


if __name__ == '__main__':
    cli()

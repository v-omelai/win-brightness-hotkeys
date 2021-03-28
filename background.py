import shlex
import subprocess

import click


@click.command()
@click.option('--command', required=True, help='Command to be executed in background')
def run_in_background(command: str):
    subprocess.Popen(shlex.split(command),
                     shell=True,
                     stdin=subprocess.DEVNULL,
                     stdout=subprocess.DEVNULL,
                     stderr=subprocess.DEVNULL)


if __name__ == '__main__':
    run_in_background()

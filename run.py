import os.path
import subprocess

import click
from dotmap import DotMap
from tinydb import TinyDB

from main import wrapper


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class CMD:
    CONSTANTS = DotMap()

    CONSTANTS.SCRIPTS.SELF = f'""{os.path.abspath(__file__)}""'
    CONSTANTS.SCRIPTS.SHORTCUT = f'""{os.path.join(BASE_DIR, "shortcut.py")}""'
    CONSTANTS.SCRIPTS.BACKGROUND = f'""{os.path.join(BASE_DIR, "background.py")}""'
    CONSTANTS.SCRIPTS.MAIN = f'""{os.path.join(BASE_DIR, "main.py")}""'

    CONSTANTS.VENV.ACTIVATE = f'""{os.path.join(BASE_DIR, "venv", "Scripts", "activate.bat")}""'

    @classmethod
    def pythonw_kill(cls):
        return subprocess.run('taskkill /f /t /im pythonw.exe', shell=True)

    @classmethod
    def pythonw_run_with_flags(cls, **kwargs):
        flags = ' '.join([f'--{flag} ""{value}""' for flag, value in kwargs.items()])
        command = f'pythonw {cls.CONSTANTS.SCRIPTS.BACKGROUND} ' \
                  f'--command "call {cls.CONSTANTS.VENV.ACTIVATE} && pythonw {cls.CONSTANTS.SCRIPTS.MAIN} {flags}"'
        return subprocess.run(command, shell=True)

    @classmethod
    def pythonw_kill_and_run_with_flags(cls, **kwargs):
        return cls.pythonw_kill(), cls.pythonw_run_with_flags(**kwargs)

    @classmethod
    def create_or_update_shortcut(cls, name: str = 'win-brightness-hotkeys'):
        path = '"' + os.path.join(
            '%APPDATA%', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup', f'{name}.lnk'
        ) + '"'
        target = f'"{os.path.join("C:", "Windows", "System32", "cmd.exe")}"'
        command = f'python {cls.CONSTANTS.SCRIPTS.SHORTCUT} ' \
                  f'--path {path} ' \
                  f'--target {target} ' \
                  f'--arguments "/c call {cls.CONSTANTS.VENV.ACTIVATE} && {cls.CONSTANTS.SCRIPTS.SELF}"'
        return subprocess.run(command, shell=True)


class Handler:
    def __init__(self, db_name: str = 'db.json', shortcut: bool = False, reset: bool = False):
        self.DB_ABSOLUTE_PATH = os.path.join(BASE_DIR, db_name)
        self.IS_EXISTS_BEFORE_LOAD = os.path.isfile(self.DB_ABSOLUTE_PATH)
        self.DB = TinyDB(self.DB_ABSOLUTE_PATH)
        self.IS_CREATED = False if reset else all([self.IS_EXISTS_BEFORE_LOAD, self.DB.all()])

        if shortcut:
            CMD.create_or_update_shortcut()

        if reset:
            self.DB.drop_tables()

        if self.IS_CREATED:
            self.run()
        else:
            self.create_and_run()

    def run(self):
        first = self.DB.all()[0]
        CMD.pythonw_kill_and_run_with_flags(**first)

    def create_and_run(self):
        def callback(**kwargs):
            self.DB.insert(kwargs)
            CMD.pythonw_kill_and_run_with_flags(**kwargs)
        wrapper(callback=callback)


@click.command()
@click.option('--shortcut', default=False, is_flag=True, help='Creates a shortcut to launch at startup')
@click.option('--reset', default=False, is_flag=True, help='Database reset')
def cli(**kwargs):
    """
    For more reference see:

    TinyDB: https://tinydb.readthedocs.io/en/latest/usage.html#advanced-usage

    CLI: https://click.palletsprojects.com/en/7.x/options/
    """
    Handler(**kwargs)


if __name__ == '__main__':
    cli()

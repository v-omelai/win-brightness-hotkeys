import operator

import click
import keyboard
import pythoncom
import wmi


def brightness(action: str, step: int):
    actions = {'+': operator.add, '-': operator.sub}
    if action not in actions.keys():
        raise Exception(f'Not supported: {action}')
    pythoncom.CoInitialize()  # noqa
    wmi_ = wmi.WMI(namespace='wmi')
    props, methods = wmi_.WmiMonitorBrightness()[0], wmi_.WmiMonitorBrightnessMethods()[0]
    current, level = props.CurrentBrightness, props.Level
    new = actions[action](current, step)
    if min(level) <= new <= max(level):
        methods.WmiSetBrightness(new, 0)


def bind(decrease: str, increase: str, step: int):
    keyboard.add_hotkey(decrease, brightness, args=('-', step))
    keyboard.add_hotkey(increase, brightness, args=('+', step))
    keyboard.wait()


def wrapper(callback=bind):
    @click.command(context_settings=dict(ignore_unknown_options=True, allow_extra_args=True))  # Workaround for run.py
    @click.option('--decrease', default='ALT+F10', show_default=True,
                  prompt='Hotkey to decrease brightness (-)', help='Hotkey to decrease brightness (-)')
    @click.option('--increase', default='ALT+F11', show_default=True,
                  prompt='Hotkey to increase brightness (+)', help='Hotkey to increase brightness (+)')
    @click.option('--step', type=int, default=20, show_default=True,
                  prompt='Brightness step', help='Brightness step')
    def cli(*args, **kwargs):
        """
        For more reference see:

        WMI: https://docs.microsoft.com/windows/win32/wmicoreprov/

        Hotkey: https://github.com/boppreh/keyboard#keyboard.add_hotkey

        CLI: https://click.palletsprojects.com/en/7.x/options/
        """
        callback(*args, **kwargs)
    cli()


if __name__ == '__main__':
    wrapper()

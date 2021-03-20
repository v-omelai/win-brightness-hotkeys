import operator
import pythoncom
import keyboard
import wmi


def brightness(action: str, step: int = 20):
    actions = {'+': operator.add, '-': operator.sub}
    if action not in actions.keys():
        raise Exception(f'Not supported: {action}')
    pythoncom.CoInitialize()
    wmi_ = wmi.WMI(namespace='wmi')
    props, methods = wmi_.WmiMonitorBrightness()[0], wmi_.WmiMonitorBrightnessMethods()[0]
    current, level = props.CurrentBrightness, props.Level
    new = actions[action](current, step)
    if min(level) <= new <= max(level):
        methods.WmiSetBrightness(new, 0)


if __name__ == '__main__':
    keyboard.add_hotkey('f10', brightness, args='-')
    keyboard.add_hotkey('f11', brightness, args='+')
    keyboard.wait()

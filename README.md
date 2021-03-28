# win-brightness-hotkeys

## Change your screen brightness by hotkeys (OS Windows solution)

![](https://img.shields.io/github/license/v-omelai/win-brightness-hotkeys)

```diff
! Feel free to modify and use, but do so at your own risk (see LICENSE)
```

## Running:
 - ### One-time: 
    - Run `main.py` with or without args
 - ### One-time in the background: 
    - Run `run.bat` without args
 - ### On a startup in the background:
    - Modify `decrease`, `increase` and `step` variables in the `run.bat`
    - Remove (or comment) the lines with `set /p` and `pause` in the `run.bat`
    - Go to the `C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`
    - Create a shortcut for `run.bat`
 
## Help:
   - main.py --help
   - background.py --help

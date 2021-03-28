@echo off
call vars.bat
%py-ver%
%project-activate-or-init%
rem Default values
set "decrease=ALT+F10"
set "increase=ALT+F11"
set "step=20"
rem Input values
set /p "decrease=Hotkey to decrease brightness (-) [%decrease%]: "
set /p "increase=Hotkey to increase brightness (+) [%increase%]: "
set /p "step=Brightness step [%step%]: "
rem Run in background
set "command=%venv-activate% && pythonw main.py --decrease ""%decrease%"" --increase ""%increase%"" --step ""%step%"""
pythonw background.py --command "%command%"
pause

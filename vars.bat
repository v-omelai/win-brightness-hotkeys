@echo off
rem Virtual environment shortcuts
set "venv-create=python -m venv venv"
set "venv-activate=call venv/Scripts/activate.bat"
set "venv-activate-safe=if exist venv %venv-activate%"
set "venv-remove=rd /s /q venv"
rem Pip shortcuts
set "pip-upgrade=python -m pip install --upgrade pip"
set "pip-install-reqs=pip install -r requirements.txt"
rem Project shortcuts
set "project-init=%venv-create% && %venv-activate% && %pip-upgrade% && %pip-install-reqs%"
set "project-activate-or-init=%venv-activate-safe% && if not exist venv start /b /wait cmd /c ""%project-init%"""
rem Other shortcuts
set "py-ver=python --version"
set "kill-pythonw=taskkill /f /t /im pythonw.exe"

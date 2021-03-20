@echo off
python --version
set "venv-create=python -m venv venv"
set "venv-activate=call venv/Scripts/activate.bat"
set "pip-upgrade=python -m pip install --upgrade pip"
set "pip-install-reqs=pip install -r requirements.txt"
if not exist venv %venv-create% && %venv-activate% && %pip-upgrade% && %pip-install-reqs%
if exist venv %venv-activate%
python background.py --command "%venv-activate% && pythonw main.py"
pause

@echo off
taskkill /f /t /im pythonw.exe
call venv/Scripts/deactivate.bat
rd /s /q venv
del /f "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\win-brightness-hotkeys.lnk"
pause

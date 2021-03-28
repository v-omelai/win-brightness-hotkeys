@echo off
rem Get admin
set "params=%*"
cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %systemdrive% 1>nul 2>nul || (  echo Set UAC = CreateObject^("Shell.Application"^) : UAC.ShellExecute "cmd.exe", "/k cd ""%~sdp0"" && %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" && "%temp%\getadmin.vbs" && exit /B )
rem Do other stuff
call vars.bat
set /p "yesno-kill-pythonw=Kill pythonw processes ([Y]/N)? "
if /i "%yesno-kill-pythonw%" neq "N" %kill-pythonw%
set /p "yesno-venv-remove=Remove venv folder ([Y]/N)? "
if /i "%yesno-venv-remove%" neq "N" %venv-remove%
pause

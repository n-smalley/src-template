@echo off
setlocal

REM Directory where this script lives (.setup_files)
set SCRIPT_DIR=%~dp0
if "%SCRIPT_DIR:~-1%"=="\" set SCRIPT_DIR=%SCRIPT_DIR:~0,-1%

REM Parent directory (project root)
for %%I in ("%SCRIPT_DIR%\..") do set PROJECT_ROOT=%%~fI

REM Paths
set VENV_DIR=%PROJECT_ROOT%\.venv
set VENV_PYTHON=%VENV_DIR%\Scripts\python.exe
set REQUIREMENTS=%SCRIPT_DIR%\requirements.txt

REM Ensure python exists
where python >nul 2>&1 || (
    echo ERROR: python not found on PATH
    exit /b 1
)

REM Create venv if missing
if not exist "%VENV_PYTHON%" (
    echo CREATING VIRTUAL ENVIRONMENT @ %VENV_DIR%
    python -m venv "%VENV_DIR%"
)

REM Activate venv (for user convenience only)
call "%VENV_DIR%\Scripts\activate.bat"

REM Upgrade pip using venv python
"%VENV_PYTHON%" -m pip install --upgrade pip

REM Install dependencies
if exist "%REQUIREMENTS%" (
    echo INSTALLING DEPENDENCIES %REQUIREMENTS%
    "%VENV_PYTHON%" -m pip install -r "%REQUIREMENTS%" --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --default-timeout=1000
) else (
    echo ERROR: requirements.txt not found
    exit /b 1
)

echo.
echo Setup complete.
echo Python in use:
"%VENV_PYTHON%" --version

endlocal

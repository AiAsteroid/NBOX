@echo off

set DIR=%~dp0system

set PATH=%DIR%\git\bin;%DIR%\python;%DIR%\python\Scripts;system\python\Lib\site-packages\torch\lib;%DIR%\ffmpeg;%DIR%\cuda;%DIR%\cuda\lib;%DIR%\cuda\bin
set PY_LIBS=%DIR%\python\Scripts\Lib;%DIR%\python\Scripts\Lib\site-packages
set PY_PIP=%DIR%\python\Scripts
set SKIP_VENV=1
set PIP_INSTALLER_LOCATION=%DIR%\python\get-pip.py
set TRANSFORMERS_CACHE=%DIR%\transformers-cache

set CUDA_PATH=%DIR%\cuda\bin

set HF_HUB_DISABLE_SYMLINKS_WARNING=1
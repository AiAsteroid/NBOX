@echo off

call environment.bat

set CUDA_MODULE_LOADING=LAZY

set appdata=tmp
set userprofile=tmp
set temp=tmp

cd %~dp0facefusion
call python run.py --execution-providers cuda cpu --skip-download --open-browser
pause

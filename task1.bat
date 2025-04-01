@echo off
REM This script sets up a virtual environment and runs the test suite for task1.
REM It checks if the virtual environment already exists, and if not, it creates one and installs the required packages.
if not exist .\venv\Scripts\activate.bat (
    echo "Creating virtual environment..."
    python -m venv venv
    .\venv\Scripts\pip install -r requirements.txt
)
REM run the test suite
.\venv\Scripts\pytest .\task1\test_generate_pyramid.py
@echo on
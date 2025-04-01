echo off
if not exist venv\Scripts\activate.bat (
    echo "Creating virtual environment..."
    python -m venv venv
    .\venv\Scripts\pip install -r requirements.txt
)
.\venv\Scripts\pytest task1/test_generate_pyramid.py
echo on
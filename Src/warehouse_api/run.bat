@echo off
echo Installing dependencies...
pip install -r requirements.txt

echo Starting server...
uvicorn main:app --reload

pause

@echo off
echo Initializing Git repository for Group 8 PV Monitor Project...
echo.

REM Initialize Git repository
git init

REM Add all files
git add .

REM Create initial commit
git commit -m "Initial commit: Photovoltaic Panel Parameter Monitor Project

- STM32F042K6 microcontroller code
- ST7735 LCD display driver
- ADC voltage measurement implementation
- Project documentation and build instructions
- Team information and project summary"

echo.
echo Git repository initialized successfully!
echo.
echo Next steps:
echo 1. Create a new repository on GitHub
echo 2. Add remote: git remote add origin [your-github-repo-url]
echo 3. Push: git push -u origin main
echo.
pause
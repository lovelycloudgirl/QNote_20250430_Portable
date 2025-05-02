@echo off
chcp 65001
setlocal

echo.
echo 🐶 歡迎使用 Q寶筆記神器安裝器
echo ------------------------------------

REM 安裝位置
set TARGET=%USERPROFILE%\Q寶筆記神器
mkdir "%TARGET%"
xcopy * "%TARGET%" /E /Y

cd /d "%TARGET%"

echo 🐾 正在建立資料夾...
mkdir outputs
mkdir assets

echo 🐾 正在安裝所需 Python 套件...
pip install -r requirements.txt

echo 🐾 正在建立桌面捷徑...
call create_shortcut.bat

echo ✅ 安裝完成！Q寶準備好了～汪！
pause

start "" "%TARGET%\Q寶筆記神器.exe"

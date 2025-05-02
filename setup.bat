@echo off
chcp 65001
setlocal enabledelayedexpansion

echo.
echo 🐶 歡迎使用 Q寶筆記神器安裝器
echo ------------------------------------
echo 🍃 葉子飄落中…
ping -n 2 127.0.0.1 >nul
echo      🍃
ping -n 2 127.0.0.1 >nul
echo    🍃
ping -n 2 127.0.0.1 >nul
echo  🍃
ping -n 1 127.0.0.1 >nul

REM 安裝位置
set TARGET=%USERPROFILE%\Q寶筆記神器
mkdir "%TARGET%"
xcopy * "%TARGET%" /E /Y
cd /d "%TARGET%"

echo 🐾 建立資料夾...
mkdir outputs
mkdir assets

echo 🐾 安裝所需 Python 套件...
pip install -r requirements.txt

echo 🐾 建立桌面捷徑...
call create_shortcut.bat

echo 🎉 安裝完成！Q寶已經就定位囉！
:: 播放提示音（需有 bark.wav）
powershell -c (New-Object Media.SoundPlayer "assets\\bark.wav").PlaySync()

pause
start "" "%TARGET%\Q寶筆記神器.exe"

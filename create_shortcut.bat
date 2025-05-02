@echo off
setlocal enabledelayedexpansion

set SHORTCUT_NAME=Q寶筆記神器
set TARGET=%~dp0Q寶筆記神器.exe
set ICON=%~dp0assets\qdog.ico

:: 建立桌面捷徑
powershell -command ^
 "$s=(New-Object -COM WScript.Shell).CreateShortcut('$env:USERPROFILE\\Desktop\\%SHORTCUT_NAME%.lnk');^
 $s.TargetPath='%TARGET%';^
 $s.IconLocation='%ICON%';^
 $s.Save()"

echo [Q寶提醒] 捷徑已經放到桌面上囉～汪！
pause

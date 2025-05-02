@echo off
chcp 65001
setlocal

echo ❌ Q寶筆記神器移除工具
echo -------------------------

set FOLDER=%USERPROFILE%\Q寶筆記神器
set SHORTCUT=%USERPROFILE%\Desktop\Q寶筆記神器.lnk

echo 🔁 正在刪除資料夾：%FOLDER%
rmdir /s /q "%FOLDER%"

echo 🗑️ 正在刪除桌面捷徑…
del "%SHORTCUT%"

echo ✅ 已完成移除，再見啦～汪！
pause

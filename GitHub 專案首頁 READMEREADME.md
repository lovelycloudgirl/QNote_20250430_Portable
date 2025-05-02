# 🐶 Q寶筆記神器 Portable v1.0

> 汪～任務完成，這是今天的會議紀錄！  
> 🎤 一鍵轉錄、說話人分離、GPT 摘要、報告輸出，全靠 Q寶！

---

## 📦 功能特色

- 🎧 WhisperX 語音辨識（支援中文）
- 👥 說話人分離（Speaker Diarization）
- ✍️ GPT 自動摘要與重點整理（支援 GPT-4）
- 📄 自動匯出 .docx 報告（含封面、逐字稿、條列、摘要）
- 🎨 草綠＋貴賓狗主題風格
- 🖼️ 封面插圖＋桌面捷徑 icon
- 🐾 支援長達 3 小時的音檔（會自動切段）

---

## 🚀 如何使用

1. 下載或 clone 本專案
2. 安裝依賴套件（Python 環境建議使用 3.9+）：
   ```bash
   pip install -r requirements.txt
# 🐶 Q寶筆記神器 Portable v1.0

> 汪～任務完成，這是今天的會議紀錄！  
> 🎤 一鍵轉錄、說話人分離、GPT 摘要、報告輸出，全靠 Q寶！

---

## 📦 功能特色

- 🎧 WhisperX 語音辨識（支援中文）
- 👥 說話人分離（Speaker Diarization）
- ✍️ GPT 自動摘要與重點整理（支援 GPT-4）
- 📄 自動匯出 .docx 報告（含封面、逐字稿、條列、摘要）
- 🎨 草綠＋貴賓狗主題風格
- 🖼️ 封面插圖＋桌面捷徑 icon
- 🐾 支援長達 3 小時的音檔（會自動切段）

---

## 🚀 如何使用

1. 下載或 clone 本專案
2. 安裝依賴套件（Python 環境建議使用 3.9+）：
   ```bash
   pip install -r requirements.txt
3.執行主程式：
python main.py
4.或雙擊 Q寶筆記神器.exe（可執行版本）

5.點選音檔，並輸入 GPT API 金鑰開始處理

6.結果將匯出至 outputs/ 資料夾
💰 GPT 費用提醒
本工具會呼叫 OpenAI GPT API

使用 GPT-4 處理會議逐字稿，每 1000 字約 NT$0.4～1

請確認你的 API 金鑰可用且額度充足
📁 輸出檔案內容
封面頁（Q寶圖＋說明）

說話人逐字稿（含時間戳）

條列式會議記錄

會議摘要段落
📂 專案結構
QNote_20250430_Portable/
├─ main.py
├─ whisper_process.py
├─ summarizer.py
├─ docx_exporter.py
├─ create_shortcut.bat
├─ config.json
├─ README_Q寶使用說明.txt
├─ README.md
├─ assets/
│   ├─ qdog.png
│   └─ qdog.ico
└─ outputs/
🧠 技術使用
WhisperX（語音辨識 + 語者分離）

OpenAI GPT-4（會議摘要）

Python + tkinter（GUI）

python-docx（Word 匯出）

PowerShell（捷徑建立）
💚 製作 & 授權
開發：lovelycloudgirl + ChatGPT 🐾
圖示靈感：Q寶（草綠貴賓狗）
使用與修改自由，歡迎 Fork 💡

---

📌 完成這個 `README.md` 之後，你的 GitHub 倉庫就完整又漂亮 ✅  
需要我幫你打包 `.zip` 給朋友測試？或要我幫你準備 PyInstaller 打包成 `.exe` 也沒問題！

要我做下一步嗎？比如：
- 幫你補一份 `requirements.txt`
- 教你打包成 `.exe`？
- 產出一鍵測試版？

你說一聲，我就幫 Q寶再升級！🐶📦

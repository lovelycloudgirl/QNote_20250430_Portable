import tkinter as tk
from tkinter import filedialog, messagebox
from whisper_process import process_audio
from summarizer import summarize_text
from docx_exporter import export_to_docx
import os

class QNoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🐶 Q寶筆記神器")
        self.root.geometry("600x400")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="歡迎使用 Q寶筆記神器！", font=("Microsoft JhengHei", 18))
        self.label.pack(pady=20)

        self.select_btn = tk.Button(self.root, text="選擇音檔", command=self.select_file)
        self.select_btn.pack(pady=10)

        self.start_btn = tk.Button(self.root, text="開始處理", command=self.start_processing)
        self.start_btn.pack(pady=10)

    def select_file(self):
        self.filepath = filedialog.askopenfilename(filetypes=[("音訊檔", "*.mp3 *.wav *.m4a")])
        if self.filepath:
            messagebox.showinfo("Q寶", f"已選擇：{self.filepath}")

    def start_processing(self):
        if not hasattr(self, "filepath"):
            messagebox.showwarning("錯誤", "請先選擇一個音檔！")
            return

        self.label.config(text="Q寶正在努力聽會議中～🐾")
        text = process_audio(self.filepath)                      # WhisperX 處理
        summary = summarize_text(text)                           # GPT 摘要
        export_to_docx(summary, self.filepath)                   # 匯出 Word
        self.label.config(text="🎉 完成啦！Q寶幫你整理好了！")
        messagebox.showinfo("完成", "處理完成，請至 outputs 資料夾查看！")

if __name__ == "__main__":
    root = tk.Tk()
    app = QNoteApp(root)
    root.mainloop()

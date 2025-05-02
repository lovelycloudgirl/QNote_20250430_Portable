import os
import subprocess
import tempfile

def process_audio(audio_path):
    # 自動建立 outputs 資料夾
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

    # 呼叫 WhisperX 指令（需預先安裝好）
    temp_txt = os.path.join(tempfile.gettempdir(), "qnote_raw.txt")
    cmd = [
        "whisperx",
        audio_path,
        "--model", "medium",
        "--language", "zh",
        "--diarize",
        "--output_dir", output_dir,
        "--output_format", "txt",
        "--compute_type", "int8",
        "--hf_token", os.getenv("HF_TOKEN", "")
    ]
    print(f"執行指令：{' '.join(cmd)}")
    subprocess.run(cmd)

    # 抓出產生的字幕 txt 檔案（逐字稿用）
    txt_files = [f for f in os.listdir(output_dir) if f.endswith(".txt")]
    if not txt_files:
        return "[Q寶提醒] 沒找到字幕輸出！"

    with open(os.path.join(output_dir, txt_files[0]), "r", encoding="utf-8") as f:
        text = f.read()

    return text

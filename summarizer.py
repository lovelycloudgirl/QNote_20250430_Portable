import openai
import os

def summarize_text(full_text):
    openai.api_key = get_api_key()

    prompt = f"""
你是一個會議記錄助手。請根據以下逐字稿進行整理，輸出包含：
1. 條列式重點
2. 會議摘要（不超過 150 字）

逐字稿內容如下：
---------------------
{full_text}
---------------------
請開始輸出：
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.5
        )
        result = response["choices"][0]["message"]["content"]
        return result

    except Exception as e:
        return f"[Q寶錯誤] GPT 摘要失敗：{e}"

def get_api_key():
    # 優先讀 config.json 中的 api_key 欄位
    import json
    config_path = "config.json"
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                return data.get("api_key", "")
            except:
                return ""
    return os.getenv("OPENAI_API_KEY", "")

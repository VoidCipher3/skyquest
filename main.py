import os
import sys

# 嘗試讀取隱藏的程式碼腳本
secret_code = os.environ.get("SCRIPT")

if not secret_code:
    print("Error: No script found.")
    sys.exit(1)

# 執行隱藏的腳本
try:
    # 這裡會執行所有 requests, json 處理, 邏輯判斷
    exec(secret_code)
except Exception as e:
    print(f"Execution Error: {e}")
    sys.exit(1)
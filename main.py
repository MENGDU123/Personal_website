import os
import time
from config import port
from config import files

print("\033[1;33m[WARN]在开始之前，请检查设置是否正确\033[0m")
time.sleep(1)
print("[INFO]",f"服务器端口:{port}",f"服务器工作路径:{files}",sep=" ")
time.sleep(1)
input("请按回车键开始...")

os.system(f"python3 -m http.server {port}")

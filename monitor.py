import psutil
import time

def now(): #用于获取当前时间，并转换为可读的方式
    import time
    # 获取当前时间的时间戳
    current_timestamp = time.time()
    # 将时间戳转换为本地时间
    local_time = time.localtime(current_timestamp)
    # 格式化时间
    formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
    return formatted_time

# 不断获取 CPU 使用率
while True:
    time.sleep(1)
    cpu_usage = psutil.cpu_percent(interval=1)
    notice = f"当前 CPU 使用率：{cpu_usage}%"
    print(now(),notice)

    with open('example.txt', 'w', encoding='utf-8') as f:
        f.write(notice)
        #明天使用一个列表，同时展示30s的状态
import psutil

print(f"CPU Usage: {psutil.cpu_percent()}%")
print(f"memory Usage: {psutil.virtual_memory().percent}%")
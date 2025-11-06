# 25. Find files larger than 1 GB
import os
for root, dirs, files in os.walk("."):
    for file in files:
        path = os.path.join(root, file)
        if os.path.getsize(path) > 1 * 1024**1:
            print(path)

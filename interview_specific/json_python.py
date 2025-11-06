import json

data = {"fruit": "apple", "color": "red"}
json_str = json.dumps(data)   # dict → JSON string
print(json_str.split(",")[0])
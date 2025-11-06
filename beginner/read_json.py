import json
try:
    with open('test.json') as file:
        data = json.load(file)

    print(data) 
    print("Name: ",data["name"])     
    print("Hobbies:", data["hobbies"])
    print("Reading:" ,data["hobbies"][0])
    print("Hiking:" ,data["hobbies"][1])
except  FileNotFoundError:
        print("File Not found error")      
except json.JSONDecodeError:
    print("Error: Invalid JSON format in 'example.json'.")        


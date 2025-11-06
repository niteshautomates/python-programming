import json
try:
    with open('complex_json.json') as file:
        data = json.load(file)
    print("\n************************** Company *******************************************\n")
    print("Company: ",data["company"])
    print("\n************************** Departments *******************************************\n")
    print("Departments: ",data["company"]["departments"])
    print("\n************************** Employees *******************************************\n")
    print("Employees: ",data["company"]["departments"][0])


    print("\n************************** Using Loops *******************************************\n")

    company = data["company"]
    for cmp in company["departments"]:
        print(f"Department: {cmp["name"]}")
        if "employees" in cmp:
            employees = cmp["employees"]
            for emp in employees:
                print(f"Employee: {emp['firstName']} {emp['lastName']}")
                if "projects" in emp:
                    for proj in emp["projects"]:
                        print("   Project:", proj["name"], "| Status:", proj["status"])
                if "skills" in emp:
                    counter = 1
                    for skill in emp["skills"]:
                        
                        print(f"{counter}.",skill)
                        counter += 1


except FileNotFoundError:
    print("File not found...")        
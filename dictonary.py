person ={ "name":"vivek", "age":25}

person["students"] = "scince"

# print(person.get("name"))
# print(person)


for value in person.items():
    print(value["name"])
    
    # if(person[value] == "grade")
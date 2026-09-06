
def check_grade(marks):
    if(marks >= 90):
        return "A"
    elif(marks >= 75 and marks < 90):
        return "B"
    elif(marks >= 50 and marks < 75):
        return "C"
    else:
        return "Fail"


print("res",check_grade(90))
print("res 1",check_grade(70))

print("res 2",check_grade(40))



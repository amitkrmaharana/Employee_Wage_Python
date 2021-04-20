import random

isAbsent = 0


def employee_check():
    # Using Random To check if Employee is Absent or Present
    random_check = random.randint(0, 2)
    if random_check == isAbsent:
        print("Employee is Absent")
    else:
        print("Employee is Present")


employee_check()

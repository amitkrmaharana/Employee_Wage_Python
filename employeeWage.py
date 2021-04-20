import random

isAbsent = 0
WAGE_PER_HOUR = int(20)
FULL_DAY_HOUR = int(8)


def employee_wage():
    # Using Random To check if Employee is Absent or Present
    random_check = random.randint(0, 2)
    if random_check == isAbsent:
        print("Employee is Absent")
    else:
        daily_wage = int(WAGE_PER_HOUR * FULL_DAY_HOUR)
        print("Employee is Present And Earns Rs.{}".format(daily_wage))


employee_wage()

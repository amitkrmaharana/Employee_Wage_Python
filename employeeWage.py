import random

isAbsent = 0
isFullTime = 1
isPartTime = 2
WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
PART_TIME_HOUR = 4


def emp_hr_check(emp_hr):
    # using switch case statements
    switcher = {
        1: FULL_DAY_HOUR,
        2: PART_TIME_HOUR
    }
    return switcher.get(emp_hr, 0)  # returns the employee hour and 0 represents the default value


def employee_wage():
    monthly_wage = 0
    for day in range(0, 20):
        # Using Random To check if Employee is Absent or Present
        random_check = random.randint(0, 3)  # random numbers from 0 to 3 excluding 3
        emp_hr = emp_hr_check(random_check)  # returned employee working hour
        daily_wage = emp_hr * WAGE_PER_HOUR  # calculated daily employee wage
        monthly_wage += daily_wage

    print("Monthly wage for the employee is Rs.", monthly_wage)


employee_wage()

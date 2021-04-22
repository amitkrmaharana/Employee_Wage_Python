import random


class EmpWageBuilder:
    IS_ABSENT = 0
    IS_PART_TIME = 1
    IS_FULL_TIME = 2

    # constructor
    def __init__(self, company_name, wage_per_hour, max_working_hours, max_working_days):
        self.company_name = company_name
        self.wage_per_hour = wage_per_hour
        self.max_working_hours = max_working_hours
        self.max_working_days = max_working_days

    def calculate_emp_wage(self):
        total_working_days = 0
        total_working_hours = 0
        monthly_wage = 0
        while total_working_days < self.max_working_days and total_working_hours < self.max_working_hours:
            # Using Random To check if Employee is Absent or Present
            attendance_check = random.randint(0, 3)  # random numbers from 0 to 3 excluding 3
            emp_hr = EmpWageBuilder.emp_hr_check(attendance_check)  # returned employee working hour
            total_working_hours += emp_hr
            total_working_days += 1
            daily_wage = emp_hr * self.wage_per_hour  # calculated daily employee wage
            monthly_wage += daily_wage
        print("Employee works in ", self.company_name)
        print("Monthly wage for the employee is Rs.", monthly_wage)
        print("Total number of days worked in a month is ", total_working_days)
        print("Total number of hours worked in a month is ", total_working_hours)

    @staticmethod  # static methods are those methods which are bound to a class rather than to its object
    def emp_hr_check(emp_hr):
        # get_emp_hr is a dictionary data type here
        get_emp_hr = {
            EmpWageBuilder.IS_PART_TIME: 4,
            EmpWageBuilder.IS_FULL_TIME: 8
        }
        return get_emp_hr.get(emp_hr, 0)  # returns the employee hour and 0 represents the default value


employee1 = EmpWageBuilder("Microsoft", 20, 60, 20)
employee2 = EmpWageBuilder("IBM", 15, 70, 23)
employee1.calculate_emp_wage()
employee2.calculate_emp_wage()

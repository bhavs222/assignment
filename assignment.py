# pgm to employee wage
print("Welcome to EmployeeWage Computation Program on Main Branch")

#pgm to absent or present 
import random
attendance = random.randint(0, 1)
if attendance == 1:
    print("Employee is Present")
else:
    print("Employee is Absent")

#pgm to daily employee wage
import random
hourly_rate = 20  
min_hours_worked = 1  
max_hours_worked = 8  
hours_worked = random.randint(min_hours_worked, max_hours_worked)
daily_wage = hourly_rate * hours_worked
print("Hours worked:", hours_worked)
print("Daily wage of employee:", daily_wage)




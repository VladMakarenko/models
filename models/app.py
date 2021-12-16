
from models.ProgClass import Programmer
from models.RecrutClass import Recruiter


a = Recruiter("Ivanov", "Ivan", "asd@gmail", "911", 1000)
b = Programmer("Petrov", "Petr", "adasdasda@gmail", "102", 5000)

print('Salary recruiter = ' + str(a.check_salary(12)))
print('Salary programmer = ' + str(b.check_salary(12)) + '\n')

print(a.level_salary(1000, 5000))

print(a.__str__())
print(b.__str__())

print(a.work())
print(b.work())
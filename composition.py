# Example of composition

class Salary:
    def __init__(self, pay):
        self.pay=pay

    def get_total(self):
        return self.pay*12


class Employee:
    def __init__(self, pay, bonus):
        self.pay=pay
        self.bonus=bonus
        self.obj_salary=Salary(self.pay)

    def annual_salary(self):
        return 'Total salary annual including bonus = £' + str(self.obj_salary.get_total() + self.bonus)

employee1=Employee(100,10)
print(employee1.annual_salary())

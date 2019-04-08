# Example of aggregation

class Salary:
    def __init__(self, pay):
        self.pay=pay

    def get_total(self):
        return self.pay*12


class Employee:
    def __init__(self, pay, bonus):
        self.pay=pay
        self.bonus=bonus

    def annual_salary(self):
        return 'Total salary annual including bonus = £' + str(self.pay.get_total() + self.bonus)

salary1=Salary(100)
employee1=Employee(salary1,10)
print(employee1.annual_salary())

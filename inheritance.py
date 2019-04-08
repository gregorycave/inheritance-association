# Example of inheritance

class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_name(self):
        return self.name + " " + self.surname

    def test(self):
        return 'Hello' 


class Employee(Human):
    def __init__(self, name, surname, employee_no):
        self.name = name
        self.surname = surname
        self.employee_no=employee_no

    def get_info(self):
        return self.name + " " + self.surname + " " + self.employee_no

human1=Human('Bob','Smith')
employee1=Employee('Gary', 'Davis', '777')

print(human1.get_name())
print(employee1.get_name())
print(employee1.get_info())
print(employee1.test())
             

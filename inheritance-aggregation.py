#Example of inheritance and aggregation
#forming a link between the employee and the department

class Department:
    def __init__(self, dept_id, subject):
        self.dept_id=dept_id
        self.subject=subject

    def get_dept_details(self):
        return 'Department ID: {0}\n Department Name: {1}\n'.format(self.dept_id,self.subject)

class Person:
    def __init__(self, name, surname):
        self.name=name
        self.surname=surname
        

class Employee(Person):
    def __init__(self, name, surname, employee_id, role, dept_id):
        super().__init__(name,surname)
        self.employee_id=employee_id
        self.dept_id=dept_id 
        self.role=role
               

    def Employee_details(self):
        return ' Name: {0}\n Employee ID: {1}\n {2}\n'.format(self.name,self.employee_id, self.dept_id.get_dept_details()) #dept_id has a link to The Department Class
                                                                                          


department1=Department('IT','IT Department')          #create an instance of Department
department2=Department('FD','Finance Department')

employee1=Employee('Bob','Smith','001','IT Assistant',department1) #when creating the Employee instance, include the department instance to form the link
employee2=Employee('Gary','Davis','002','Accountant',department2)

print(employee1.Employee_details())                               #call a method from the Employee class, this includes the department details
print(employee2.Employee_details())

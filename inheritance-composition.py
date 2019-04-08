#Example of inheritance and composition
#An employee incurs training costs 

class Person:
    def __init__(self, name, surname):
        self.name=name
        self.surname=surname
        

class Employee(Person):
    def __init__(self, name, surname, employee_id, provider, location, cost, travel):
        super().__init__(name,surname)
        self.employee_id=employee_id
        self.provider=provider
        self.location=location
        self.cost=cost
        self.travel=travel
        self.training=TrainingCost(self.cost,self.travel) #call a class from within a class


    def employee_details(self):
        return 'Name: {0}\nEmployee ID: {1}\nProvider: {2}\nTotal Cost: {3}\n'.format(self.name,self.employee_id,self.provider,self.training.calculate_total_cost())
        
            
class TrainingCost:
    def __init__(self, cost, travel):
        self.cost=cost
        self.travel=travel           
        
    def calculate_total_cost(self):
        return self.cost + self.travel


employee1=Employee('Bob','Smith','001','AWS','London',10,28.50)
employee2=Employee('Gary','Davis','002','CFA','Sydney',16,37.34)

print(employee1.employee_details())
print(employee2.employee_details())

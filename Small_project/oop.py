class Workers:
    def __init__(self,name,job,salary):
        self.name = name
        self.job = job
        self.salary = salary

    def Worker_Display(self):
        return self.name, self.job, self.salary


worker1 = Workers(name="John", job="Cashier", salary=50000)
worker2 = Workers(name="Alice", job="Waiter", salary=60000)
worker3 = Workers(name="Bob", job="Chef", salary=70000)
worker4 = Workers(name="Eve", job="Cashier", salary=55000)

class Managers:
    def __init__(self,name,job,salary):
        self.name = name
        self.job = job
        self.salary = salary

    def Manager_Display(self):
        return self.name, self.job, self.salary

    def Add_salary(self, amount):
        self.salary += amount
        return self.salary

manager1 = Managers(name="David", job="Manager", salary=80000)
manager2 = Managers(name="Sarah", job="Manager", salary=90000)

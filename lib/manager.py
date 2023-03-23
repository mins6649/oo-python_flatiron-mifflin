from lib.employee import Employee

class Manager:

    all = []

    def __init__(self, name, department, age):
        self.name = name
        self.department = department
        self.age = age
        Manager.all.append(self)

    def get_name(self):
        return self.name
    
    def get_department(self):
        return self.department
    
    def get_age(self):
        return self.age
    
    def get_employees(self):
        return [emp.name for emp in Employee.all if emp.manager == self]
    
    def hire_employee(self, name, salary):
        Employee(name, salary, self)

    @classmethod
    def all_departments(cls):
        return [man.department for man in cls.all]
    
    @classmethod 
    def average_age(cls):
        
        # age_count = 0
        # for i in cls.all:
        #     age_count += i.age
        # return (age_count) / len(cls.all)

        age_list = [man.age for man in cls.all]
        return sum(age_list) / len(age_list)

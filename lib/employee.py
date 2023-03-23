class Employee:

    all = []

    def __init__(self, name, salary, manager):
        self.name = name
        self.salary = salary
        self.manager = manager
        Employee.all.append(self)
        
    def get_name(self):
        return self.name
    
    def get_salary(self):
        return self.salary
    
    def get_manager_name(self):
        return self.manager.name
    
    @classmethod
    def paid_over(cls, num):
        return [emp.name for emp in cls.all if emp.salary > num]
    
    @classmethod
    def find_by_department(cls, department):
        return [emp for emp in cls.all if emp.manager.department == department][0]
    
    def tax_bracket(self):
        return [emp.name for emp in Employee.all if (self.salary + 1000 ) >= emp.salary >= (self.salary - 1000) ]



class Employ :
    startTime = "10Pm"
    end_time = "5Pm"


class AdminStaff(Employ):
    def __init__(self, role):
        self.role = role 
    

class Accountant (AdminStaff):
    def __init__(self, salary, role):
        super().__init__(role)
        self.salary = salary 

a1 = Accountant(25_000, "CA")
print(a1.role , a1.salary)
        
        


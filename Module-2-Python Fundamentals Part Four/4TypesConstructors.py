




class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa
    
    def get_cgpa(self):
        return self.cgpa
    
stu1 = Student("rakibul", 9.23)
stu2 = Student("Hasan",5.34)
stu3 = Student("Hasibul",5.23)

print(stu1.get_cgpa())

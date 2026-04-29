class Employ :
    startTime = "10Pm"
    end_time = "5Pm"

    def ChangeTheTime(self , new_end_time):
        self.end_time = new_end_time

class Teacher (Employ):
    def __init__(self, subject):
        self.subject = subject
        

t1 = Teacher("Math")
t1.ChangeTheTime("11AM")

print(t1.subject)
print(t1.end_time)

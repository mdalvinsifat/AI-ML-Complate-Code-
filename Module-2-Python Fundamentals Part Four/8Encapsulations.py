class BankAccount :
    def __init__(self, name, balance):
        self.name = name 
        self._balance = balance #protect


b1 = BankAccount("ruhal Kumar", 500)


print(b1.name , b1._balance)












class BankAccount :
    def __init__(self, name, balance):
        self.name = name 
        self.__balance = balance #privet
    
    def getinset(self):
        return self.__balance


c1 = BankAccount("ruhal Kumar", 500)


print(c1.name , c1.getinset())

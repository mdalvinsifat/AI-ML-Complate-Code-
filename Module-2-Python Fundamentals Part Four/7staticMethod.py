class Laptop:
    storage_type = "ssd"

    def __init__(self, ram, storage):
        self.storage = storage
        self.ram = ram 
    
    @classmethod
    def getStorage(cls):
        print(f"storage type = {cls.storage_type}")
    
    def get_info(self):
        print(f"Laptop {self.ram} Ram {self.storage} and {self.storage_type}")

    @staticmethod
    def cal_amount(price, discount):
        final_price = price - (discount * price / 100)
        print(f"discount price : {final_price}")


l1 = Laptop("16GB", "512GB")

l1.cal_amount(40000, 20)
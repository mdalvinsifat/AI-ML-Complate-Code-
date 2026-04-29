class Laptop :
    storage_type = "ssd"

    def __init__(self, ram,storage):
        self.storage = storage
        self.ram = ram 
    
    @classmethod
    def getStorage(cls):
        print(f"storage type = {cls.storage_type}")
    
    def get_info(self):
        print(f"Laptop {self.ram} Ram {self.storage} and {self.storage_type}")



l1 = Laptop("16gb", "512Gb")


l1.getStorage()
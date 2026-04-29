
class Laptop :
    storage_type = "ssd"

    def __init__(self, ram,storage):
        self.storage = storage
        self.ram = ram 
     
    def get_info(self):
        print(f"Laptop {self.ram} Ram {self.storage} and {self.storage_type}")



l1 = Laptop("16gb", "512Gb")
l2 = Laptop("8gb", "256Gb")

l1.get_info()
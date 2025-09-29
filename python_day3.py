class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand {self.brand} and model {self.model}")

class Truck(Vehicle):
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)
        self.load_capacity = load_capacity

    def display_info(self):
        print(f"Brand {self.brand}, model {self.model} and Load capacity {self.load_capacity}")

# creating objects
truck1 = Truck("VW", "5.1", "56kg")
truck2 = Vehicle("VW", "6.2")
truck1.display_info()
truck2.display_info()
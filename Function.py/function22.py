class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def get_make(self):
        return self.make
    
    def get_model(self):
        return self.model

my_car = Car("Toyota", "Corolla")
print(my_car.get_make())   # Output: Toyota

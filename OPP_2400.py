class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_on = False
        self.is_accelerating = False
        self.is_braking = False

    def start(self):
        self.is_on = True

    def accelerate(self):
        self.is_accelerating = True

    def brake(self):
        self.is_braking = True

    def status(self):
        print(f"Brand: {self.brand}\nModel: {self.model}\nOn: {self.is_on}\nAccelerating: {self.is_accelerating}\nBraking: {self.is_braking}")

    def move(self):
        print("I move using an indeterminate number of wheels.")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.__chassis_length = 250
        self.__chassis_width = 120
        self.__wheels = 4

    def start(self):
        self.is_on = True
        check = self.__internal_check()
        if self.is_on and check:
            return "The car is running."
        elif self.is_on and not check:
            return "Something went wrong in the check. We cannot start."
        else:
            return "The car is stopped."

    def status(self):
        super().status()
        print(f"Chassis length: {self.__chassis_length} cm\nChassis width: {self.__chassis_width} cm\nWheels: {self.__wheels}")

    def __internal_check(self):
        print("Performing internal check")
        self.fuel = "ok"
        self.oil = "ok"
        self.doors = "closed"
        return self.fuel == "ok" and self.oil == "ok" and self.doors == "closed"

    def move(self):
        print("I move using four wheels.")

class Motorcycle(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.wheelie_state = ""

    def wheelie(self):
        self.wheelie_state = "I'm doing a wheelie"

    def status(self):
        super().status()
        print(f"Wheelie: {self.wheelie_state}")

    def move(self):
        print("I move using two wheels.")

class Truck(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.__wheels = 6

    def move(self):
        print("I move using six wheels.")

# Polymorphic function
def vehicle_move(vehicle):
    vehicle.move()

# Usage
my_car = Car("Toyota", "Corolla")
my_motorcycle = Motorcycle("Honda", "CBR")
my_truck = Truck("Volvo", "FH")

print(my_car.start())
my_car.status()
print()

my_motorcycle.wheelie()
my_motorcycle.start()
my_motorcycle.status()
print()

my_truck.start()
my_truck.status()
print()

for v in [my_car, my_motorcycle, my_truck]:
    vehicle_move(v)

# Vehicle Inheritance and Polymorphism in Python 

This project was created as part of a university course on Object-Oriented Programming (OOP) comp 2400. The code demonstrates key OOP concepts such as:

- Classes and objects  
- Inheritance  
- Encapsulation  
- Polymorphism  
- Special methods (`__init__`, `super()`, private methods)

## Code Structure

- `Vehicle`: Base class that defines common properties and methods for any type of vehicle.
- `Car`: Inherits from `Vehicle` and adds specific features like chassis length, width, and internal check.
- `Motorcycle`: Inherits from `Vehicle` and adds the ability to perform a wheelie.
- `Truck`: Inherits from `Vehicle` and implements its own movement behavior.
- `vehicle_move(vehicle)`: A polymorphic function that shows how different vehicles implement their movement.

## Example Usage

```python
my_car = Car("Toyota", "Corolla")
print(my_car.start())
my_car.status()

my_motorcycle = Motorcycle("Honda", "CBR")
my_motorcycle.wheelie()
my_motorcycle.status()

my_truck = Truck("Volvo", "FH")
my_truck.status()

for v in [my_car, my_motorcycle, my_truck]:
    vehicle_move(v)

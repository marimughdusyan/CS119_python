# Mari Mughdusyan
# CS 119 programming in python
# Lab 10 Car class


# define a car class
class Car:
    def __init__(self, year_model, make):
        # attributes
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # method to add 5 to the speed
    def accelerate(self):
        self.__speed += 5

    # method to subtract 5 from the speed
    def brake(self):
        self.__speed -= 5

    # get the speed
    def get_speed(self):
        return self.__speed


# make an object
myCar = Car(2025, "KIA")

# add 5 to speed 5 times and display the current speed
for i in range(5):
    myCar.accelerate()
    print(myCar.get_speed())

# subtract 5 from the speed 5 times and display the current speed
for i in range(5):
    myCar.brake()
    print(myCar.get_speed())

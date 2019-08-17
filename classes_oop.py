# OOP features

class Car(): # in class name follow CamelCase format
    """general class for a model of a car"""
    __maxspeed = 150 

    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
        self.odometer_reading = 0
    
    def get_descriptive_name(self, color = 'white'):
        """returns the full desc of the car"""
        print(f"Car description: {color} {self.year} {self.make} {self.model}")

    def get_odometer_reading(self):
        """returns total milage of the car"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def set_odometer(self, milage):
        """sets the odometer of the car, raject if milage is less than current milage"""
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can not roll back odometer.")

    def increment_odometer(self, miles):
        # self.odometer_reading = self.odometer_reading + miles
        if miles >=0 :
            self.odometer_reading += miles
        else: 
            print("You can not add negative miles to odomter")

    def get_maxspeed(self):
        print(f"Maximum speed in this car is : {self.__maxspeed}.")

    def set_maxspeed(self, speed):
        self.__maxspeed = speed

    def fill_gas_tank(self):
        print("Filling your gas tank ...")
    
    def drive(self):
        print('driving..')


# INHERITANCE - inherits the contructor and the behaviour of the parent class 
class ElectricCar(Car):
    """Represents the aspects of a car, specific to an electric car"""

    def __init__(self, year, make, model):
        """Initialize attributes of the parent class and specific to electric car."""
        super().__init__(year, make, model)
        self.battery_size = 80

    def get_battery_size(self):
        """returns the size of battery"""
        print(f"battery size : {self.battery_size}-kWh.")

    def set_battery_size(self, battery_size):
        if battery_size >= self.battery_size :
            self.battery_size = battery_size
        else:
            print(f"You can not update the battery for less than {self.battery_size}-kwh")
    # __maxspeed is not accessible even to child class
    # def udpate_maxspeed(self, speed):
    #     self.__maxpeed = speed

    def fill_gas_tank(self):
        print("Electric cars do not have gas tank.")

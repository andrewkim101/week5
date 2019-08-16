# EXECUTION 

# importing specific class from module
# from classes_oop import * 
from classes_oop import Car, ElectricCar

# importing the whole module
import hello
# greet() # this will not work 
hello.greet()

# ------- default constructor (before creating the __init__ in the Car class )
# camry = Car() 
# camry.year = 2018
# camry.make = 'toyota'
# camry.model = 'camry'

camry = Car(2018, 'toyota', 'camry')
camry.get_descriptive_name()

# ----- accessing the attributes directly 
camry.odometer_reading = 1000
camry.get_odometer_reading()
# camry.odometer_reading = 900
# camry.set_odometer(900)

# accessing (updating) the attribute through methos, you can put some logic 
camry.set_odometer(2000)
camry.get_odometer_reading()

camry.increment_odometer(200)
camry.get_odometer_reading()

camry.increment_odometer(-200)
camry.get_odometer_reading()
print("==============================")
# ------
# inheritance, encapsulation, polymorphism, method overriding 

# polymorphism - using the same methods from different classes or using the same method with diff. attributes
print(len('hello'))
print(len([4, 5, 6, 712, 3453456, 23 ]))
camry.get_descriptive_name()
camry.get_descriptive_name('black')

# encapsulation - concept of hiding or limiting the access to certain methods or variables in the class
# create the instance variable in the class >> __maxspeed
# camry.__maxspeed = 200  
camry.set_maxspeed(200)
camry.get_maxspeed()


# ELECTRIC CAR - tests for child class of Car class
my_tesla = ElectricCar(2019, 'tesla', 'model s')
print(my_tesla.battery_size)
my_tesla.get_descriptive_name()
my_tesla.get_battery_size()
my_tesla.set_battery_size(70)
my_tesla.get_battery_size()
my_tesla.set_battery_size(100)
my_tesla.get_battery_size()

my_tesla.set_maxspeed(210)

# method(function) overriding, overriding inheritted function in child class
camry.fill_gas_tank()
my_tesla.fill_gas_tank()

bmw = Car(2019, 'bmw', '530-i')

# Sets the variable "cars" equal to the value of 100.
cars = 100
# Sets the variable "space_in_a_car" equal to the value of 4.0.
space_in_a_car = 4.0
# Sets the variable "drivers" equal to the value of 30.
drivers = 30
# Sets the variable "passengers" equal to the value of 90.
passengers = 90
# Sets the variable "cars_not_driven" equal to the result of "cars" minus "drivers".
cars_not_driven = cars - drivers
# Sets the variable "cars_driven" equal to the variable "drivers".
cars_driven = drivers
# Sets the variable "carpool_capacity" equal to the result of "cars_driven" multiplied by "space_in_a_car".
carpool_capacity = cars_driven * space_in_a_car
# Sets the variable "average_passengers_per_car" equal to the result of "passengers" divided by "cars_driven".
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

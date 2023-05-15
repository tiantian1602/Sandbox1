from unreliable_car import UnreliableCar

# Create a new unreliable car object, my_unreliable_car, with name "Beatle", 100 units of fuel and reliability of 50%
my_unreliable_car = UnreliableCar("Beatle", 100, 50)

# Attempt to drive the car 40 km
driven_distance = my_unreliable_car.drive(40)

# Print the car's details and the actual distance driven
print(my_unreliable_car)
print(f"Attempted to drive 40km, actually drove {driven_distance}km")

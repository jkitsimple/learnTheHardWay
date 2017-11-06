name = 'Zach Smith'
age = 26
height = 70 # inches
weight = 167 # lbs
height_cm = height * 2.54
weight_kg = weight * 0.454
eyes = 'Hazel'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall. Which is {height_cm} cm!")
print(f"He's {weight} pounds heavy. This is the same as {weight_kg} kg.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right.
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# creates a parameterized string 'x'
types_of_people = 10
x = f"There are {types_of_people} types of people."

# Kinda silly, but initializing string 'literals' and including them into double quoted strings "".. looks like using the 'f' operator allows you to inject a variable into a double quoted string using the '{}' syntax.
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

# Print the strings x & y
print(x)
print(y)

# Injecting the string 'x' into the new double quoted string inside the #print method
print(f"I said {x}")
print(f"I also said: '{y}'")

# Injecting the boolean var into 
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# Ah, Here we see the String#format method in action.. taking a parameter 'hilarious' and injecting it into the first placeholder {} it finds
print(joke_evaluation.format(hilarious))

# intializing 2 strings and then concatening them in the #print method
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

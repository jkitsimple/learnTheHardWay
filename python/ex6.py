# Creates the variable "types_of_people" sets it equal to the value 10.
types_of_people = 10
# Creates the variable "x" and sets it equal to the f-string below containing the previously defined variable "types_of_people".
x = f"There are {types_of_people} types of people."

# Creates the variable "binary" and sets it equal to the string below.
binary = "binary"
# Creates the variable "do_not" and sets it equal to the string below.
do_not = "don't"
# Creates the variable "y" and sets it equal to the f-string below containing the previously defined variables "binary" and "do_not".
y = f"Those who know {binary} and those of {do_not}."

# Displays the variables "x" and "y" to the console.
print(x)
print(y)

# Displays the f-string below containing the variable "x".
print(f"I said: {x}.")
# Displays the f-string below containing the variable "y".
print(f"I also said: '{y}'")

# Creates the variable "hilarious" and sets it equal to "False".
hilarious = False
# Createst the variable "test" and sets it equal to the string "Maybe".
test = "Maybe"
# Creates the variable "joke_evaluation" and sets it equal to the string below containing two empty sets of curly brackets {}. These sets of curly brackets act as retainers for variables to be added in later.
joke_evaluation = "Isn't that joke so funny?! {} {}"

# Displays the variable "joke_evaluation" to the console containing the variables "hilarious" and "test" in the locations where the empty curly brackets are above.
print(joke_evaluation.format(hilarious, test))

# Creates the variable "w" and sets it equal to the string below.
w = "This is the left side of..."
# Creates the variable "e" and sets it equal to the string below.
e = "a string with a right side."

# Displays the variables "w" and "e" together on the same line. Essentially creating one sentence from the two different strings.
print(w + e)

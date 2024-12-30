# Intro to Python Class Template
# This script covers variables, input, strings, lists, if-else, for loops, while loops, and functions.

# By Eric Utomo, December 2024

# VARIABLES
name = "randomStudent"  # String variable
grade = 8  # Integer variable
is_excited = True  # Boolean variable

print(f"Hello, {name}! Welcome to Python class for grade {grade}.")

# INPUT
name = input("What's your name? ")
is_excited = input("Are you excited to learn Python? (yes/no) ").lower() == "yes"

if is_excited:
    print(f"That's awesome, {name}! Let's dive in.")
else:
    print(f"No worries, {name}. Hopefully, you'll enjoy it as we go!")

# STRINGS AND LISTS
favorite_things = []  # Empty list
print("Let's create a list of your three favorite things.")
for i in range(3):
    thing = input(f"Enter favorite thing #{i + 1}: ")
    favorite_things.append(thing)

print("Here's your list of favorite things:")
for thing in favorite_things:
    print(f"- {thing}")

# IF-ELSE
if "Python" in favorite_things:
    print("Python is one of your favorite things! That's great!")
else:
    print("Hmm, Python isn't on your list. Maybe it'll make it there soon!")

# WHILE LOOP
print("\nLet's play a guessing game!")
secret_number = 7
attempts = 0
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1
    if guess == secret_number:
        print(f"Congratulations, {name}! You guessed it in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

# FUNCTIONS
def display_summary():
    print("\nSUMMARY OF WHAT YOU LEARNED:")
    print("1. Variables to store information like your name and grade.")
    print("2. Input to interact with the user.")
    print("3. Strings and lists to manage and display text and collections of items.")
    print("4. If-else statements to make decisions.")
    print("5. For loops and while loops for repetition.")
    print("6. Functions like this one to organize your code.")

display_summary()

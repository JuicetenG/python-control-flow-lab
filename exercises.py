# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()


# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    print('enter a letter:')
    letter = input().lower()

    if len(letter) != 1:
        print('you entered too many charaters')
        return
    
    if not letter.isalpha():
        print('wrong data type entered')
        return

    if letter in ('a', 'e', 'i', 'o', 'u'):
        print(f'the letter {letter} is a vowel')
    else:
        print(f'the letter {letter} is a consonant')
# Call the function
check_letter()


# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    print('please enter your age')
    age = input()
    
    try:
        age = int(age)
        if age <= 0:
            print('enter a number greater than 0')
            return 
        elif age > 0 and age < 18:
            print('you are too young to vote')
        else:
            print('Go vote!')
    except ValueError:
        print('please enter a number')
    
# Call the function
check_voting_eligibility()


# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years. 
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.


def calculate_dog_years():
    # Your control flow logic goes here
    dog_age = input("enter your dog's age: ")
    dog_years = 0

    try: 
        dog_age = int(dog_age)

        if dog_age <= 0: 
            print('enter a number greater than 0')
            return
    
        if dog_age < 0:
            print('enter a positive number')
            return
        
        while dog_age > 0:
            if dog_age > 2:
                dog_years += 7
            else:
                dog_years += 10

            dog_age -= 1
  
    except ValueError:
        print('Please enter a number')
        return
    
    print(f"The dog's age in dog years is {dog_years}")

# Call the function
calculate_dog_years()


# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Your control flow logic goes here
    print('is it cold today? (enter \'yes\' or \'no\')')
    is_cold = input().lower()
    print('is it raining today? (enter \'yes\' or \'no\')')
    is_raining = input().lower()
    
    if is_cold != 'yes' and is_cold != 'no':
        print('please enter \'yes\' or \'no\'')
        return

    if is_raining != 'yes' and is_raining != 'no':
        print('please enter \'yes\' or \'no\'')
        return

    if is_cold == 'yes' and is_raining == 'yes':
        print('wear a raincoat')
    
    if is_cold == 'yes' and is_raining == 'no':
        print('wear a warm coat')

    if is_cold == 'no' and is_raining == 'yes':
        print('bring an umbrella')

    if is_cold == 'no' and is_raining == 'no':
        print('wear light clothing')
    
# Call the function
weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Your control flow logic goes here
    print('enter month of the year (jan - dec)')

    month = input().lower()
    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    if month not in months:
      print('invalid month format, please enter 3 letter abbreviation')
      return

    print('enter day of month')

    day = input()
    try: 
      day = int(day)
    except ValueError:
      print('invalid input for day')
      return
    
    if day > 31:
      print('what month has this many days???')
      return

    if month == "dec" and day >= 21 or month in ["jan", "feb"] or month == "mar" and day <= 19:
        season = "Winter"
    elif month == "mar" and day >= 20 or month in ["apr", "may"] or month == "jun" and day <= 20:
        season = "Spring"
    elif month == "jun" and day >= 21 or month in ["jul", "aug"] or month == "sep" and day <= 21:
        season = "Summer"
    else:
        season = "Fall"
    
    print(f'{month.capitalize()} {day} is in {season}')
# Call the function
determine_season()
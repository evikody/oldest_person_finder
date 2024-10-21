def valid_name(user_name): # Define a function named "valid_name" to validate each names inputted
    # Use .isalpha to check if "user_name" contains only alphabetic letters
    return user_name.isalpha() # Returns True if all characters in the string are in the alphabet

# Ask the user to input their name and age.
user_name = input("Please enter your name: ")
user_age = int(input("PLease enter your age: "))
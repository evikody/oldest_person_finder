def valid_name(user_name): # Define a function named "valid_name" to validate each names inputted
    # Use .isalpha to check if "user_name" contains only alphabetic letters
    return user_name.isalpha() # Returns True if all characters in the string are in the alphabet

# Loop 1: This will continue asking for input until the user enters a valid name
while True:
        user_name = input("Please enter your name: ") # Ask the user to input their name

        if valid_name(user_name): #If valid, it breaks out of the loop and moves on to the next part of the program
            break
        else: #If invalid, it prints an error message and repeats the process
            print("Error: Please enter a valid name.")

user_name = input("Please enter your age: ") # Ask the user to input their age


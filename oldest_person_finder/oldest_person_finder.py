def valid_name(user_name): # Define a function named "valid_name" to validate each name inputted
    # Use .isalpha to check if "user_name" contains only alphabetic letters
    return user_name.isalpha() # Returns True if all characters in the string are in the alphabet

def valid_age(user_age): # Define a function named "valid_age" to validate each age inputted
    # Use .isdigit to check if "user_age" contains only digits
    return user_age.isdigit()

records = [] # The collected information will store here

# Loop 3: A loop to collect user input
while True:

    # Loop 2: This will continue asking for input until the user enters a valid name
    while True:
        user_name = input("Please enter your name: ") # Ask the user to input their name

        if valid_name(user_name): #If valid, it breaks out of the loop and moves on to the next part of the program
            break
        else: #If invalid, it prints an error message and repeats the process
            print("Error: Please enter a valid name.")

    # Loop 3: This will continue asking for input until the user enters a valid age
    while True:
        user_age = (input("Please enter your age: ")) # Ask the user to input their age

        if valid_age(user_age): # If valid
            break # It breaks out of the loop and moves on to the next part of the program
        else: # If invalid
            print("Error: Please enter a valid age.") # It prints an error message and repeats the process

    # Store valid inputs in the list
    records.append({"name": user_name, "age": user_age})

    retry = input("Do you want to enter another entry? Yes or No: ") # Ask if the user wants to continue
    if retry == 'No': # If the user responds with No
        break # Exit the loop

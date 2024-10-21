def valid_name(user_name): # Define a function named "valid_name" to validate each name inputted
    # Use .isalpha to check if "user_name" contains only alphabetic letters and .split for spacings
    # Use char in ["'", " "] to allow apostrophes and spaces
    return all(char.isalpha() or char in ["'", " "] for char in user_name) # Returns True if all characters in the string are in the alphabet

def valid_age(user_age): # Define a function named "valid_age" to validate each age inputted
    # Use .isdigit to check if "user_age" contains only digits
    return user_age.isdigit() # Returns True if all characters in the string are digits

records = [] # The collected information will store here

# Loop 1: A loop to collect user input
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

    # Loop 4: This will continue asking until the user enter a proper Yes or No
    while True:
        retry = input("Do you want to enter another entry? Yes or No: ") # Ask if the user wants to continue
        # If the first letter is not capitalized, print the error and loop again
        if retry.lower() == "yes" or retry.lower() == "no":
            if retry != "Yes" and retry != "No":
                print("The first letter should be capitalized (Yes/No).")
            else:
                break  # Properly capitalized "Yes" or "No"
        else:
            print("Invalid input. Please type Yes or No.")

    if retry == "No":
        break  # Stop asking for entries if the user says "No"

if records: # Check if the list is not empty
    oldest_person = records[0] # Assume that the first person is the oldest
    for person in records: # Loop through all the person in the list
        if person["age"] > oldest_person["age"]: # Compare their age
            oldest_person = person # If the current person is older, update oldest_person
    print(f"The oldest person is {oldest_person['name']} with age {oldest_person['age']}.")
else:
    # If the 'records' list is empty, inform the user that no data was collected
    print("No data collected.")
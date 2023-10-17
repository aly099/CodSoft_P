# import the 'random' and 'string' modules for generating random characters
import random
import string

# define the 'generate_password' function that takes a length as input
def generate_password(length):
    # Define character sets for password complexity
    lowercase = string.ascii_lowercase  # set of lowercase letters
    uppercase = string.ascii_uppercase  # set of uppercase letters
    digits = string.digits  # set of digits
    special_characters = string.punctuation  # set of special characters

    # Combine character sets based on complexity
    if length < 8:  # if length is less than 8, use a simpler character set
        charset = lowercase + uppercase + digits
    else:  # if length is 8 or more, include special characters for complexity
        charset = lowercase + uppercase + digits + special_characters

    # Generate the password by randomly selecting characters from the character set
    password = ''.join(random.choice(charset) for _ in range(length))
    return password  # return the generated password

# define the 'main' function
def main():
    print("Welcome to the Password Generator!")  # display a welcome message
    length = int(input("Enter the desired password length: "))  # get user input for the desired password length
    
    if length < 1:  # check if the entered length is valid
        print("Invalid password length. Please enter a positive number.")
    else:  # if the length is valid, generate the password and display it
        password = generate_password(length)
        print("Generated Password: ", password)  # display the generated password

# check if the script is being run directly
if __name__ == "__main__":
    main()  # call the 'main' function

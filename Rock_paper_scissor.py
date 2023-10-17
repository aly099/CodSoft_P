# Import the 'random' module for generating random choices
import random

# Define a function to determine the winner based on the choices
def determine_winner(user_choice, computer_choice):
    # Check for a tie
    if user_choice == computer_choice:
        return "It's a tie!"
    # Check for the winning conditions for the user
    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "scissor" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    # If the user doesn't win, they lose
    else:
        return "You lose!"

# Define the main function for the game
def main():
    # List of available choices
    choices = ["rock", "paper", "scissor"]
    
    # Loop to continue playing until the user decides to stop
    while True:
        # Get the user's choice and ensure it is valid
        user_choice = input("Enter your choice (rock, paper, scissor): ").lower()
        while user_choice not in choices:
            user_choice = input("Invalid choice. Please choose from rock, paper, or scissor: ").lower()

        # Generate a random choice for the computer
        computer_choice = random.choice(choices)

        # Display the choices of the user and the computer
        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        # Determine and display the winner
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

# Check if the script is being run directly
if __name__ == "__main__":
    main()  # Call the 'main' function to start the game

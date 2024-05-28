import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You win!"
    else:
        return "Computer wins!"

choices = ['Rock', 'Paper', 'Scissors']
user_choice = input("Enter your choice (Rock, Paper, Scissors): ")
if user_choice not in choices:
    print("Invalid choice. Please choose Rock, Paper, or Scissors.")
else:
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

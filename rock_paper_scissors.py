import random

print("Welcome to Rock, Paper, Scissors!")
print("Type 'quit' anytime to exit.\n")



while True:
    user_choice = input("Enter rock, paper, or scissors:")

    if user_choice.lower() == "quit":
        print("Thanks for your time try actually playing next time bitch")
        break

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    computer_number = random.randint(1, 3)
    if computer_number == 1:
        computer_choice = "rock"

    elif computer_number == 2:
        computer_choice = "paper"

    elif computer_number == 3:
        computer_choice = "scissors"

    print(f'You: {user_choice}.')
    print(f"Bot: {computer_choice}.")

    if user_choice == computer_choice:
        print("It's a tie!")

    elif user_choice == "rock" and computer_choice == "scissors":
        print("You Win rock beats scissors!")

    elif user_choice == "rock" and computer_choice == "paper":
        print("you lose paper beats rock!")

    elif user_choice == "paper" and computer_choice == "rock":
        print("You win paper beats rock!")

    elif user_choice == "paper" and computer_choice == "scissors":
        print('You lose scissors beats paper!')

    elif user_choice == "scissors" and computer_choice == "paper":
        print('You win scissors beats paper!')

    elif user_choice == "scissors" and computer_choice == "rock":
        print('You lose rock beats scissors!')

    again = input("Would you like to play again? (y/n): ")

    while True:
        if again.lower() == "y":
            break

        elif again.lower() == "n":
            print("Thank you for playing!")
            exit()

        else:
            print('Please enter y or n.')




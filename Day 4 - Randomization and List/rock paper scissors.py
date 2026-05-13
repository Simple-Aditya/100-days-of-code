import random
print("Welcome to Rock, Paper, Scissors!")
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

computer_choice = random.randint(0, 2)
choice_dict = {0: "Rock", 1: "Paper", 2: "Scissors"}
print(f"Computer chose {choice_dict[computer_choice]}")

if choice == computer_choice:
    print("It's a draw!")
elif (choice == 0 and computer_choice == 2) or (choice == 1 and computer_choice == 0) or (choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")



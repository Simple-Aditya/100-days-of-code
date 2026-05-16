import random

title = r'''
   _____                       _   _                 _               
  / ____|                     | \ | |               | |              
 | |  __ _   _  ___  ___ ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/ |_| \_|\__,_|_| |_| |_|_.__/ \___|_|                                                                        
'''
easy = 15
medium = 10
hard = 5

def play_game(low=1, high=100, chances=10):
    target = random.randint(low, high)
    guessed = []
    
    print(f"I'm thinking of a number between {low} and {high}.")
    print(f"You have {chances} chances to guess it. Good luck!")

    while chances > 0:
        print(f"Chances left: {chances}")
        try:
            guess = int(input("Guess the number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess in guessed:
            print("You've already guessed that number. Try again.")
            continue
        guessed.append(guess)
        
        if guess < low or guess > high:
            print(f"Please guess a number within [{low}, {high}].")
            continue

        if guess == target:
            print(f"Correct! The number was {target}.")
            return True
        elif guess < target:
            print("Too low.")
        else:
            print("Too high.")

        chances -= 1

    print(f"Out of chances. The number was {target}.")
    return False


while True:
    print(title)
    difficulty = input("Choose difficulty (easy/medium/hard): ").strip().lower()
    if difficulty == 'easy':
        play_game(chances=easy)
    elif difficulty == 'medium':
        play_game(chances=medium)
    elif difficulty == 'hard':
        play_game(chances=hard)
    else:
        print("Invalid difficulty. Please choose again.")
        continue

    again = input("Play again? (y/n): ").strip().lower()
    print('\n' + '-' * 50 + '\n')
    if again != 'y':
        print("Thanks for playing.")
        break

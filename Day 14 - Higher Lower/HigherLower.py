title = r'''
 _   _ _       _                 _                            
| | | (_)     | |               | |                           
| |_| |_  __ _| |__   ___ _ __  | |     _____      _____ _ __ 
|  _  | |/ _` | '_ \ / _ \ '__| | |    / _ \ \ /\ / / _ \ '__|
| | | | | (_| | | | |  __/ |    | |___| (_) \ V  V /  __/ |   
\_| |_/_|\__, |_| |_|\___|_|    \_____/\___/ \_/\_/ \___|_|   
          __/ |                                               
         |___/                                                
'''

import data
import random
import os

def game():
    data_points = data.data
    
    random.shuffle(data_points)
    score = 0

    while len(data_points) > 1:
        option_a = data_points[0]
        option_b = data_points[1]

        print(f"Compare A: {option_a['name']}, a {option_a['description']}\n{option_a['value']:,} monthly active users.")
        print("VS")
        print(f"Against B: {option_b['name']}, a {option_b['description']}.")

        while guess not in ['A', 'B']:
            guess = input("Who has more monthly active users? Type 'A' or 'B': ").upper()

        if guess == 'A' and option_a['value'] >= option_b['value']:
            score += 1
            print(f"Correct! Your current score is: {score}.\n")
            data_points.pop(1)
            
        elif guess == 'B' and option_b['value'] >= option_a['value']:
            score += 1
            print(f"Correct! Your current score is: {score}.\n")
            data_points.pop(0)
            
        else:
            print(f"\nWrong! Final score: {score}.")
            print(f"{option_a['name']} has {option_a['value']:,} monthly active users.")
            print(f"{option_b['name']} has {option_b['value']:,} monthly active users.\n")
            break
    
    print("Congratulations! You've compared all the options!")
        
while True:
    print(title)
    game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    os.system('cls')
    if play_again != 'yes':
        print("Thanks for playing! Goodbye!")
        break
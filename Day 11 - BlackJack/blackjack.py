import cards
import random

title = r'''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/         
'''
print(title)
print("Welcome to the Blackjack Game!")
play_continue = True

hit = '''
┌─────────────────────────────┐
│            HIT!             │
└─────────────────────────────┘
'''
stand = '''
┌─────────────────────────────┐
│            STAND!           │
└─────────────────────────────┘
'''

card_dict = cards.cards
user_cards = []
admin_cards = []

def print_cards(cards, card_dict=card_dict):
    for card in cards:
        print(card_dict[card])
        
def calculate_total(cards):
    total = 0
    aces = 0

    for card in cards:
        rank = card.split('_')[0]

        if rank in ['J', 'Q', 'K']:
            total += 10
        elif rank == 'A':
            total += 11
            aces += 1
        else:
            total += int(rank)

    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total

while play_continue:

    deck = list(card_dict.keys())
    random.shuffle(deck)
    card1, card2 = deck.pop(), deck.pop()
    user_cards.extend([card1, card2])

    card3, card4 = deck.pop(), deck.pop()
    admin_cards.extend([card3, card4])

    print(f"Your cards: ")
    print_cards(user_cards, card_dict)
    print(f"Admin's cards: ")
    print(card_dict[admin_cards[0]])
        
    print(hit)
    print(stand)
    
    user_total = calculate_total(user_cards)
    choice = input("Do you want to hit or stand? ").strip().lower()

    while user_total < 21 and choice == "hit":
        card5 = deck.pop()
        user_cards.append(card5)
        user_total = calculate_total(user_cards)
        if user_total > 21:
            break
        
        print(f"Your cards: ")
        print_cards(user_cards, card_dict)
        print(f"Admin's cards: ")
        print(card_dict[admin_cards[0]])
        choice = input("Do you want to hit or stand? ").strip().lower()
        print(hit)
        print(stand)

        
    user_total = calculate_total(user_cards)
    admin_total = calculate_total(admin_cards)
    
    while admin_total <= 16:
        card6 = deck.pop()
        admin_cards.append(card6)
        admin_total = calculate_total(admin_cards)

    print(f"Your cards: ")
    print_cards(user_cards, card_dict)
    print(f"Admin's cards: ")
    print_cards(admin_cards, card_dict)

    print(f"Your total: {user_total}")
    print(f"Admin's total: {admin_total}")

    if user_total > 21:
        print("You went over 21. You lose!")
    elif admin_total > 21:
        print("Admin went over 21. You win!")
    elif user_total > admin_total:
        print("You win!")
    elif user_total < admin_total:
        print("You lose!")
    else:
        print("It's a tie!")
        
    play_again = input("Do you want to play again? Type 'yes' or 'no': ").strip().lower()
    if play_again == "no":
        play_continue = False
    else:
        user_cards = []
        admin_cards = []
        print("\n" * 100)
        print(title)
        print("Welcome to the Blackjack Game!")
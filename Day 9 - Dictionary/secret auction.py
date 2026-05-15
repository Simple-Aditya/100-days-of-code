title = r'''
  _______ _             _____ _ _            _                        _   _             
 |__   __| |           / ____(_) |          | |       /\             | | (_)            
    | |  | |__   ___  | (___  _| | ___ _ __ | |_     /  \  _   _  ___| |_ _  ___  _ __  
    | |  | '_ \ / _ \  \___ \| | |/ _ \ '_ \| __|   / /\ \| | | |/ __| __| |/ _ \| '_ \ 
    | |  | | | |  __/  ____) | | |  __/ | | | |_   / ____ \ |_| | (__| |_| | (_) | | | |
    |_|  |_| |_|\___| |_____/|_|_|\___|_| |_|\__| /_/    \_\__,_|\___|\__|_|\___/|_| |_|                                                                                        
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(title)
print("Welcome to the secret auction program.")
bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").strip().lower()
    
    if should_continue == "no":
        bidding_finished = True
        highest_bidder = ""
        highest_price = 0
        
        for bidder in bids:
            bid_amount = bids[bidder]
            if bid_amount > highest_price:
                highest_price = bid_amount
                highest_bidder = bidder
        
        print(f"The winner is {highest_bidder} with a bid of ${highest_price}.")
    
    elif should_continue == "yes":
        print("\n" * 100)
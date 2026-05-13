print("Welcome to the pizza store!")
size = input('''
What size pizza do you want?
Small: $5.00 (s)
Medium: $7.00 (m)
Large: $10.00 (l)\n
''')

toppings = []
toppings_need = input("Do you want to add toppings? (y/n) ")
while toppings_need.lower() == 'y':
    topping_selection = input('''
    What toppings do you want to add?
    1. Pepperoni: $1.00 (1)
    2. Mushrooms: $0.50 (2)
    3. Onions: $0.25 (3)
    4. Sausage: $1.50 (4)
    5. Bacon: $1.75 (5)
    6. Extra cheese: $1.25 (6)
    7. Black olives: $0.75 (7)
    8. Green peppers: $0.50 (8)
    ''')
    if(topping_selection not in ['1', '2', '3', '4', '5', '6', '7', '8']):
        print("Invalid topping selection.")
        continue
    toppings.append(topping_selection)
    toppings_need = input("Do you want to add more toppings? (y/n) ")

total_bill = 0
if size == 's':
    total_bill += 5
elif size == 'm':
    total_bill += 7
elif size == 'l':
    total_bill += 10
else:
    print("Invalid size selection.")
    exit()
    
for topping in toppings:
    if topping == '1':
        total_bill += 1
    elif topping == '2':
        total_bill += 0.50
    elif topping == '3':
        total_bill += 0.25
    elif topping == '4':
        total_bill += 1.50
    elif topping == '5':
        total_bill += 1.75
    elif topping == '6':
        total_bill += 1.25
    elif topping == '7':
        total_bill += 0.75
    elif topping == '8':
        total_bill += 0.50

print(f"Your total bill is: ${total_bill:.2f}")
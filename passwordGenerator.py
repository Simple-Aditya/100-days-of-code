import random

print("Welcome to the Password Generator!")
num_words = int(input("How many words would you like in your password? "))
num_numbers = int(input("How many numbers would you like in your password? "))
num_symbols = int(input("How many symbols would you like in your password? "))

words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

password_list = []
for i in range(num_words):
    password_list.append(random.choice(words))
for i in range(num_numbers):
    password_list.append(random.choice(numbers))
for i in range(num_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password = ''.join(password_list)
print(f"Your password is: {password}")
title = r'''
 __________
| ________ |
||12345678||
|""""""""""|
|[M|#|C][-]|
|[7|8|9][+]|
|[4|5|6][x]|
|[1|2|3][%]|
|[.|O|:][=]|
"----------" 
'''
def calculate():
    num1 = float(input("What's the first number?: "))
    operation = input("Pick an operation: +, -, *, /, %: ")
    num2 = float(input("What's the second number?: "))
    result = 0 

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    else:
        print("Invalid operation.")
        return
    
    print(f"{num1} {operation} {num2} = {result}")

print(title)
print("Welcome to the calculator program.")

continue_calculating = True
while continue_calculating:
    calculate()
    should_continue = input("Do you want to continue calculating? Type 'yes' or 'no'.\n").strip().lower()
    
    if should_continue == "no":
        continue_calculating = False
    elif should_continue == "yes":
        print("\n" * 100)
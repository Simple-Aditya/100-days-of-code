total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

if(people == 0):
    print("Number of people cannot be zero.")
    exit()

total_tip = total_bill * tip_percentage / 100
total_bill_with_tip = total_bill + total_tip
bill_per_person = total_bill_with_tip / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")


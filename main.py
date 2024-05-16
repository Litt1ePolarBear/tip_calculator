print("Welcome to the tip calculator!")

bill = float(input("What was the total bill?"))

percentage = int(input("what percentage tip would you like to give? 10, 12, or 15?"))

people = int(input("How many people to split the bill?"))

bill_with_tip = (bill * (100 + percentage)) / 100

final_price = float(bill_with_tip / people)

A = round(final_price,2)

print(f"Each person should pay : ${A}")

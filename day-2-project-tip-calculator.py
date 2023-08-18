print("Welcome to the tip calculator")
total_bill = float(input("What is the total bill? $"))
tip_percentage = int(input("What is the percentage tip would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill? "))

bill_with_tip = (total_bill / no_of_people) * (1 + tip_percentage / 100)
rounded_bill = "{:.2f}".format(round(bill_with_tip,2))
print(f"Each person should pay: ${rounded_bill}")
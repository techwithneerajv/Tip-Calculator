print("Welcome to the Tip Calculator.")

Total_amt = input("What is the total bill ?")

Tip_percentage = input("What percentage tip would you like to give ? 10, 12 or 15 ?")

Total_people = input("How many people to split the bill ?")

Total_tip = int(Total_amt) * int(Tip_percentage) / 100

Final = int(Total_tip) / int(Total_people)

print(f"Each person should pay: ${Final}")

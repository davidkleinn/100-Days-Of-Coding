print("Welcome to the tip calculator!")
totalBill = float(input("What was the total bill? $"))
billPercent = float(input("How much tip would you like to give? 10, 12, or 15? "))
billSplit = float(input("How many people to split the bill? "))

bill = totalBill + (totalBill * billPercent/100)
totalTip = bill / billSplit

print(f"Each person should pay: ${totalTip:.2f}")
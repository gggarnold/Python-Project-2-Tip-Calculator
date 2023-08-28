#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#TIP CALCULATOR

print("Welcome to the tip calculator")

totalbill = input("What was the total bill? $")
totalbill_as_float = float(totalbill)

percentagetip = input("What percentage tip would you like to give? 10, 12, or 15? ")
percentagetip_as_int = int(percentagetip)/100 + 1

billsplit = input("How many people to split the bill? ")
billsplit_as_int = int(billsplit)

tipanswer = (totalbill_as_float / billsplit_as_int) * percentagetip_as_int
tipanswerfloat = ("%.2f" % tipanswer)

print(f"Each person should pay ${tipanswerfloat}")

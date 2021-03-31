#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
#Create a tip calculator

print("welcome to tip calculator.")

#bill amount float value

bill_amount = float(input("What was the total bill? $"))

#tip percentage as int

tip = int(input("what percentage tip would you like to give? 10, 12, or 15? "))

#group to split amout of bill

split = int(input("How many people to split the bill? "))

#total of the amount to split 

results = (bill_amount / split) * (tip / 100 + 1)

#printed results of total

print(f"Each person should pay {round(results,2)}")

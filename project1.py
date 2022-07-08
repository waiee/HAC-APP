#Estimate House and Car Price Calculator

#Formula for house price by Wan Aizat - Agen Hartanah Lembah Klang.
#Source: Twitter

#1. Salary= Rough Salary - (EPF + Socso + tax)
#2. DSR = Clean Salary x 65% or 60% or 75%
#3. TotalLoan = DSR - (Bank Commitment)
#4. House Price = totalLoan x 200
#5. Monthly Price Limit = salary x 35%
#################################################################

print(" ------- Welcome to House & Car Price Calculator -------")
print("")
#1. Salary
print("How much is you salary? (exc EPF, Socso, & Tax):")
salary = float(input("My Salary: RM "))

dsr = float(1)

if salary < 3000:
    dsr = dsr*salary*0.60
elif salary > 5000:
    dsr = dsr*salary*0.75
else:
    dsr = dsr*salary*0.70
print("")

#2. Commitment
print("How much is your bank commitment? (Car, personal loan etc.):")
bankCom = float(input("My Bank Commitment: RM "))

#3.Total Monthly Loan
totalLoan = dsr - bankCom

#4. Estimate House Price
housePrice = totalLoan*200

#5. Loan limit (should be < 35% of salary)
loanLimit = salary*0.35

print("-----------------------------------------------------")
print("Result:")
print("")
print("Your Salary: RM", '%.2f' % salary)
print("Your Bank Commitment: RM", '%.2f' % bankCom)
print("")
print("House: ")
print("Estimated Price: RM", '%.2f' % housePrice)
print("DSR (Debt Service Ratio): RM", '%.2f' % dsr)
print("Monthly limit: RM", '%.2f' % loanLimit) 
print("")
# print("Guide: ")
# print("Your maximum house price should be: RM", '%.2f' % housePrice)
# print("Your monthly limit (35% of your salary): RM", '%.2f' % loanLimit)

#################################################################
#Formula for Car Price by Twitter

#1. carPrice = salary x 12
#2. downPayment = 20% x carPrice
#3. loanPeriod = 12 x 7
#4. monthlyLimit = 15% salary

#1. Estimate car price
carPrice = salary*12

#2. Count downpayment
downPayment = carPrice*0.20

#3. Count loan period for 7 years in months
loanPeriod = 12*7

#4. Count monthly limit 
monthlyLimit = salary*0.15

# print statement
print("Car: ")
print("Estimated Price: RM", '%.2f' %  carPrice)
print("Downpayment(20%): RM",'%.2f' %  downPayment)
print("Loan duration(7 years):", loanPeriod, "months")
print("Monthly: RM", '%.2f' % monthlyLimit)


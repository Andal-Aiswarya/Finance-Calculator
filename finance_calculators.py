import math

#Ask the user to choose which calculation they want from given option
invest_bond = input("Choose either 'investment' or 'bond' from the menu below to proceed: \ninvestment - to calculate the amount of the interest you'll earn on your interest \nbond - to calculate the amount you'll have to pay on a home loan\n")

#capitalise in all way - not to affect selection
#using if, elif condition for investment and bond
if invest_bond.lower() == "investment":

    #declare and get values for all variables required
    principle = int(input("Enter the depositing amount of money: "))
    rate = float(input("Enter the interest rate in percentage: "))
    rate = rate/100
    time = int(input("Enter the number of years: "))
    interest = input("Please select 'simple' or 'compound' interest: ")

    #formula for simple interest and print the result
    if interest.lower() == "simple":
        amount = principle * (1 + rate * time)
        amount = round(amount, 2)
        print(f"You will get total amount: {amount}")

    #formula for compound interest and print the result
    elif interest.lower() == "compound":
        amount = principle * (1 + rate) ** time
        amount = round(amount, 2)
        print(f"You will get total amount: {amount}")

    #to get invalid interest option
    else:
        print("Enter valid interest option!")


elif invest_bond.lower() == "bond":
    #declare and get values for all variables required
    present_value = float(input("Enter the present value of the house: "))
    annual_rate = float(input("Enter the annual interest rate in percentage: "))
    monthly_rate = annual_rate / (12 * 100)
    num_of_months = int(input("Enter the number of months: "))

    #formula for compound interest and print the result
    repayment = (monthly_rate * present_value) / (1 - (1 + monthly_rate) ** (- num_of_months))
    repayment = round(repayment, 2)
    print((f"You will have to repay £{repayment} per month!"))

else:
    print("Enter valid option 'investment' or 'bond' :")

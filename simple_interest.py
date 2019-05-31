import math

def simple_interest():

  int1 = input("Enter the principal: \n")

  int2 = input("Enter the rate of interest: \n")

  int3 = input("Enter the number of years: \n")

  principal = float(int1)
  rate_of_interest = float(int2)
  years = float(int3)

  rate = rate_of_interest / 100

  output = principal * (1 + (rate * years))
  end_amount = round(output,3)

  print("After " + str(years) + " years at " + str(rate_of_interest) + "%, the investment will be worth $" + str(end_amount))

simple_interest()
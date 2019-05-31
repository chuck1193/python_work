import math

def compound_interest():
  int1 = input("What is the principal amount? \n")
  int2 = input("What is the rate? \n")
  int3 = input("What is the number of years? \n")
  int4 = input("What is the number of times the interest is compounded per year? \n")

  principal = float(int1)
  rate_of_interest = float(int2)
  years = float(int3)
  times_per_year = float(int4)

  rate = rate_of_interest / 100

  output = principal * (1 + (rate / times_per_year)) ** (times_per_year * years)
  end_amount = round(output,2)

  print("$" + str(principal) + " invested at " + str(rate_of_interest) + "% for " + str(years) + " years compounded " + str(times_per_year) + " times per year is " + str(end_amount) + ".")

compound_interest()
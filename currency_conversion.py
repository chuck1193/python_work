import math

def currency_conversion():
  int1 = input("How many euros are you exchanging? ")
  int2 = input("What is the exchange rate? ")

  euros = float(int1)
  exchange_rate = float(int2)

  rate = exchange_rate / 100
  
  rate_to = round(rate,2)

  amount_to = (euros * rate_to)
  output = round(amount_to,2)

  print("You have " + str(euros) + " euros and the exchange rate is " + str(exchange_rate) + " so you will receive " + str(output) + " US dollars back.")

currency_conversion()
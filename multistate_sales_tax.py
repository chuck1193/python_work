def multistate_sales_tax():
  int1 = input("What is the order amount?\n")
  order_amount = float(int1)

  state = input("What state do you live in?\n")

  if (state == "wisoconsin" or state == "wi"):
    county = input("Which county are you in?\n")
    if (county == "eau claire"):
      sales_tax = order_amount * 0.005
      end_amount = order_amount + sales_tax
      print("Total: " + str(order_amount) + "\nTax: " + str(sales_tax) + "\nEnd Total: " + str(end_amount))
    elif (county == "dunn"):
      sales_tax = order_amount * 0.004
      end_amount = order_amount + sales_tax
      print("Total: " + str(order_amount) + "\nTax: " + str(sales_tax) + "\nEnd Total: " + str(end_amount))
    else:
      print("You total is: " + order_amount)
  elif (state == "illinois" or state == "il"):
    sales_tax = order_amount * 0.08
    end_amount = order_amount + sales_tax
    print("Total: " + str(order_amount) + "\nTax: " + str(sales_tax) + "\nEnd Total: " + str(end_amount))
  else:
    print("Total: " + str(order_amount))

multistate_sales_tax()
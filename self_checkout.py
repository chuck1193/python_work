def self_checkout():
  # item_1 = input("Enter the price of the item. ")
  # quantity_1 = input("Enter the quantity of the item. ")

  # item1 = int(item_1)
  # quantity1 = int(quantity_1)

  # price_exact1 = item1 * quantity1

  # item_2 = input("Enter the price of the item. ")
  # quantity_2 = input("Enter the quantity of the item. ")

  # item2 = int(item_2)
  # quantity2 = int(quantity_2)

  # price_exact2 = item2 * quantity2

  # item_3 = input("Enter the price of the item. ")
  # quantity_3 = input("Enter the quantity of the item. ")

  # item3 = int(item_3)
  # quantity3 = int(quantity_3)

  # price_exact3 = item3 * quantity3

  # overall_price = price_exact1 + price_exact2 + price_exact3
  # tax = overall_price * 0.055
  # output = round(tax,2)

  # total = overall_price + output

  # print("Subtotal: " + str(overall_price))
  # print("Tax: " + str(output))
  # print("Total: " + str(total))
  overall_price = 0

  while overall_price >= 0: 
    int1 = input("enter the price of the item. ")
    int2 = input("enter the quantity of the item. ")

    price = int(int1)
    quantity = int(int2)

    if (price == 0 or price == '' or quantity == 0 or quantity == ''):
      print("You did not enter the correct numbers. Try again.")
      continue

    price_exact = quantity * price
    overall_price += price_exact


    tax = overall_price * 0.055
    output = round(tax,2)

    total = overall_price + output

    keep_going = input("Are there any more items? ")
    if (keep_going == 'no'):
      break


  print("Subtotal: " + str(overall_price))
  print("Tax: " + str(tax))
  print("Total: " + str(total))



self_checkout()
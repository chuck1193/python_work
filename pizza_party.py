def pizza_party():

  int1 = input("How many people? ")

  int2 = input("How many pizzas do you have? ")

  int3 = input("How many slices are in each pizza? ")

  people = int(int1)
  number_of_pizzas = int(int2)
  slices = int(int3)

  pieces_for_each_person = (slices * number_of_pizzas
    ) / people
  leftover = (slices * number_of_pizzas) % people

  if (people == '' or number_of_pizzas == '' or slices == ''):
    print("You need to enter in a number for me to calculate how many slices each person gets to eat. ")
    pizza_party()
  elif (number_of_pizzas < 2):
    print(str(number_of_pizzas) + " pizzas for " + str(people) + " people means everyone gets " + str(pieces_for_each_person) + " piece each with " + str(leftover) + " pieces leftover.")

pizza_party()
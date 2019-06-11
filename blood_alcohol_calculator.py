def blood_alcohol():
  
  print("okay, time to calculate your blood alcohol levels!")

  int1 = input("weight:\n")
  gender = input("gender(m/f):")
  int2 = input("number of drinks:\n")
  int3 = input("how many ounces per drink:\n")
  int4 = input("amount of time that has passed since your last drink (can put decimals to represent mintues):\n")

  weight = float(int1)
  number_of_drinks = float(int2)
  ounces_per_drink = float(int3)
  time = float(int4)
  
  if (gender == 'm' or 'male'):
    BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
    if (BAC < 0.08):
      print("You are legal to drive right now.")
    else:
      print("You are not legal to drive right now.")
  elif (gender == 'f' or 'female'):
    BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
    if (BAC < 0.08):
      print("You are legal to drive right now.")
    else:
      print("You are not legal to drive right now.")

blood_alcohol()
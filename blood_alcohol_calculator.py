def blood_alcohol():
  
  print("okay, time to calculate your blood alcohol levels!")

  int1 = input("weight:\n")
  gender = input("gender(m/f):")
  int2 = input("number of drinks:\n")
  int3 = input("how many ounces per drink:\n")
  int4 = input("amount of time that has passed since your last drink (can put decimals to represent mintues):\n")
  state - input("state you live in:\n")

  weight = float(int1)
  number_of_drinks = float(int2)
  ounces_per_drink = float(int3)
  time = float(int4)

  if (state == 'alabama' or state == 'al'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'alaska' or state == 'ak'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'arizona' or state == 'az'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'arkansas' or state == 'ar'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'california' or state == 'ca'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.01):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.01):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'colorado' or state == 'co'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.08):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.08):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'connecticut' or state == 'ct'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'delaware' or state == 'de'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'washington dc' or state == 'dc'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'florida' or state == 'fl'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'georgia' or state == 'ga'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'hawaii' or state == 'hi'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'idaho' or state == 'id'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'illinois' or state == 'il'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'indiana' or state == 'in'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
  elif (state == 'iowa' or state == 'ia'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'kansas' or state == 'ks'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'kentucky' or state == 'ky'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'louisiana' or state == 'ls'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'maine' or state == 'me'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'maryland' or state == 'md'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'massachussetts' or state == 'ma'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'michigan' or state == 'mi'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'minnesota' or state == 'mn'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'mississippi' or state == 'mi'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'missouri' or state == 'mo'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'montana' or state == 'mt'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'nebraska' or state == 'ne'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'nevada' or state == 'nv'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'new hampshire' or state == 'nh'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'new jersey' or state == 'nj'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.01):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.01):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'new mexico' or state == 'nm'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.0):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.0):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'new york' or state == 'ny'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'north carolina' or state == 'nc'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'north dakota' or state == 'nd'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'ohio' or state == 'oh'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.0)2:
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'oklahoma' or state == 'ok'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'oregon' or state == 'or'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'pennsylvania' or state == 'pa'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'rhode island' or state == 'ri'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'south carolina' or state == 'sc'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'south dakota' or state == 'sd'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'tennessee' or state == 'tn'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'texas' or state == 'tx'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'utah' or state == 'ut'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'vermont' or state == 'vt'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'virginia' or state == 'va'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'washington' or state == 'wa'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'west virginia' or state == 'wv'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'wisconsin' or state == 'wi'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.00):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")

  elif (state == 'wyoming' or state == 'wy'):
    if (gender == 'm' or gender == 'male'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.73)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")
    elif (gender == 'f' or gender == 'female'):
      BAC = ((ounces_per_drink * 5.14) / (weight * 0.66)) - (0.015 * time)
      if (BAC < 0.02):
        print("You are legal to drive right now.")
      else:
        print("You are not legal to drive right now.")


blood_alcohol()
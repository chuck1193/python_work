def legal_driving():
  int1 = input("What is your age?\n")

  age = int(int1)

  if (age < 0):
    print("Please input another number.")
    legal_driving()
  elif (age < 16):
    print("You are not old enough to drive.")

  else:
    print("You are old enough to drive.")
 

legal_driving()
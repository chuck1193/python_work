def area_of_a_rectangle():

  int1 = input("What is the length of your room? ")
  choice1 = input("Is this in feet or meters? ")


  int2 = input("What is the width of your room? ")
  choice2 = input("Is this in feet or meters? ")


  if (int1 == '' or int2 == ''):
    print("You entered nothing, please try again. ")
    area_of_a_rectangle()
  elif (choice1 == 'feet' and choice2 == 'feet'):

    length = int(int1)
    width = int(int2)
    feet_squared = length * width
    square_meters = feet_squared * 0.09290304
    print("You entered the dimensions of " + str(length) + " feet and "  + str(width) + " feet.")
    print("The area is " + str(feet_squared) + " square feet.")
  elif (choice1 == 'meters' and choice2 == 'meters'):
    length = int(int1)
    width = int(int2)

    feet_squared = length * width
    square_meters = feet_squared * 0.09290304
    print("The area is " + str(feet_squared) + " square feet. " + str(square_meters) + " square meters.")

area_of_a_rectangle()
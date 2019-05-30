import math

def paint_calculator():

  round = input("Is your room round? ")

  lshaped = input("Is your room L-shaped? ")

  if (round == 0 or round == '' or lshaped == '' or lshaped == 0):
      print("You either enter in nothing or you entered a 0 and well, neither of those work so try again.")
      paint_calculator()

  elif (round == 'yes'): 
      length = input("What is the length of the room? ")
      if (length == 0 or length == ''):
        print("You entered something wrong. and need to start over again. Wonderful")
        paint_calculator()
      else:
        length2 = int(length)
        radius = length2 / 2
        area_circle = 3.14 * (radius**2)
        gall = area_circle / 350
        gallons = math.ceil(gall)
        print("You will need to purchase " + str(gallons) + " gallons of paint to paint " + str(area_circle) + " square feet of room.")
  elif (lshaped == 'yes'):
      print("To figure out the area for an L shaped room we have to divide the room into two different rectangle and then I will add them together.")
      rectangle1_length = int(input("What is the length of the first rectangle? "))
      rectangle1_width = int(input("What is the width of the first rectangle? "))

      rectangle2_length = int(input("What is the length of the second rectangle? "))
      rectangle2_width = int(input("What is the wodth of the second rectangle? "))

      area_lshaped = (rectangle1_length * rectangle1_width) + (rectangle2_length * rectangle2_width)

      gall2 = area_lshaped / 350

      gallons2 = math.ceil(gall2)

      print("You will need to purchase " + str(gallons2) + " gallons of paint to paint " + str(area_lshaped) + " square feet of ceiling.")

  else: 
      len1 = input("What is the length of the room? ")
      wid1 = input("What is the width of the room? ")

      length = int(len1)
      width = int(wid1)

      area = length * width
      gall = area / 350

      gallons = math.ceil(gall)

      print("You will need to purchase " + str(gallons) + " gallons of paint to paint " + str(area) + " square feet of room.")

paint_calculator()

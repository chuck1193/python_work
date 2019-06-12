import math

def temp_converter():
  c_or_f = input("Press 'c' to convert from Fahrnheit to Celsius. Press 'f' to convert from celsius to fahrenheit.\n")
  int1 = input("Temp:\n")

  temp = float(int1)

  if (c_or_f == 'c'):
    c = (temp - 32) * (5 / 9)
    output = round(c,0)
    print("The temperature in celsius is " + str(output))
  elif (c_or_f == 'f'):
    f = (temp * (9 / 5)) + 32
    output = round(f,0)
    print("The temperature in fahrenheit is" + str(output))

temp_converter()
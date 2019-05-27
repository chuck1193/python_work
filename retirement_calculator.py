import datetime

int1 = input("What is your current age?")
int2 = input("At what age do you want to retire?")

age = int(int1)
retirement = int(int2)

year = str(datetime.datetime.now().year)
current_year = int(year)

retirement_year = retirement - age
year_of_retirement = current_year + retirement_year

print("You have " + str(retirement_year) + " years until you can retire.")
print("It's " + str(current_year) + ", you can retire in " + str(year_of_retirement))
import random

def rock_paper_scissors():
  users_choice = input("Alright, time to choose! Rock, Paper, or Scissors? ")
  computer_choices = ["rock", "paper", "scissors"]

  computers_choices = random.choice(computer_choices)

  print ("Computer's Choice: " + computers_choices)

  if users_choice == computers_choices:
    print ("It's a tie!")
    rock_paper_scissors()
  elif users_choice == "rock":
    if computers_choices == "paper":
      print ("Computer Wins")
    else: 
      print ("You win!")
  elif users_choice == "paper":
    if computers_choices == "scissors":
      print ("Computer Wins!")
    else: 
      print ("You Win!")
  elif users_choice == "scissors":
    if computers_choices == "rock":
      print ("Computer Wins!")
    else: 
      print ("You Win!")

rock_paper_scissors()
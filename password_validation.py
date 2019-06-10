import getpass

def password_validation():
  login = input("Are you already a member?\n")

  if (login == 'no'):
    username = input("Please give me your username:\n").lower()
    password = getpass.getpass("Password:\n").lower()

    password_dict = {}
    password_dict[username] = password

    print(password_dict)

    print("Alright, now please login.\n")

    username = input("What is your username?\n")

    password = getpass.getpass("What is the password?\n")

    if (username in password_dict and password in password_dict):
      print("Welcome!")
      exit
    else:
      print(password_dict)
      print("I don't know you. Try Again.")
      password_validation()

  else:


    while login == 'yes':
      username = input("What is your username?\n")

      password = getpass.getpass("What is the password?\n")

      password_dict = {}

      if (KeyError):
        print("You are not a member. Please create an acoount and then login.\n")
        password_validation()
      elif (username == '' or password == ''):
        print("I don't know you.\n")
        print("Now we have to start all over. Great.")
      elif (username == password_dict[username] and password == password_dict[password]):
        print("Welcome!")


  

password_validation()
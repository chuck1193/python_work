import getpass
def password_validation():
  password = getpass.getpass("What is the password?\n")

  if (password == "abc$123"):
    print("Welcome!")
  else:
    print("I don't know you.")

password_validation()
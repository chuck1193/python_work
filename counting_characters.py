def counting_characters():

  words = input("Give me a word and I will tell you the length of that word. ")
  length = len(words)

  if len(words) == 0:
    print("You've given me nothing.")
    counting_characters(2)
  else: 
    print(words + " has " + str(length) + " characters.")

counting_characters()
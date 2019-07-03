def is_anagram():

  word1 = []
  word2 = []

  print("Enter two words and I'll tell you if they are anagrams:\n")
  string1 = input("Enter the first word: \n")
  string2 = input("Enter the second word:\n")

  
  # if (string1 == string2): 
  #   print("You have entered the same word trice. Try again.")
  # elif (sorted(string1) == sorted(string2)):
  #   print(string1 + " and " + string2 + " are anagrams.")
  # else: 
  #   print("These two words are not anagrams.")

  

  for x in range(len(string1)):
    word1.append(string1[x])
  for x in range(len(string2)):
    word2.append(string2[x])
  if(len(word1) == len(word2)):
    for letter in word1:
      if(letter in word2):
        word2.remove(letter)

  if (len(word2) == 0):
    print(string1 + " and " + string2 + " are anagrams.")
  else:
    print(string1 + " and " + string2 + " are not anagrams.")


is_anagram()
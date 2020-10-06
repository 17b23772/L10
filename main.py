print ("Welcome To The Vegetable Guessing Game")
print("\n")
print ("The Choices Will Be : Carrot, Broccoli, Peas, Sweetcorn")
print("\n")
print("I Will Now Attempt To Guess Your Vegetable")
print("\n")
print("Is Your Vegetable Green? Y/N")
answer = input().lower()
if answer == "y":
   print("Does it look like a tree? Y/N")
   answer = input().lower()
   if answer == "y":
     print ("Your Vegetable Is Broccoli!")
   else:
     print ("Your Vegetable Is Peas!")

else:
  print("Is Your Vegetable Orange? Y/N")
  answer = input().lower()
  if answer == "y":
    print("Your Vegetable Is A Carrot!")
  else:
    print ("Your Vegetable Is A Sweetcorn!")

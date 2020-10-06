print ("Welcome To The Vegetable And Animal Guessing Game")
print("\n")
print ("The Choices Will Be : Carrot, Broccoli, Peas, Sweetcorn. Y/N")
answer = input().lower()
if answer == "y":
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

print(" Or If Your Choosing An Animal: Lion, Ostrich, Whale. Y/N")
answer = input().lower()
else:
  print("Pick either Ostrich, Lion or Whale")
print("I will attempt to guess your choice")
print("Does the animal live in the water? Y/N")
answer = input().lower()

if answer == "n":
   print("Does the animal have wings? Y/N")
   answer = input().lower()
   if answer == "y":
       print("It must be an Ostrich!")
   else:
       print("It must be a Lion!")
else:
   print("It must be a Whale!")


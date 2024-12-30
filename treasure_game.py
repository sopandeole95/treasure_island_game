print("Welcome to Treasure Island.")

print("Your mission is to find the treasure.")

choice = input("Do you want to go left or right(L/R)? ")

if choice == "R" or choice == "r":

  print("You are dead, game over")

else:

  choice1 = input("Swim or Wait(S/W)? ")

  if choice1 == "S" or choice1 == "s":

    print("You are dead, game over")

  else:

    choice2 = input("Which door, red, blue or yellow(R/B/Y)? ")

    if choice2 == "R" or choice2 == "r":

      print("Burned by fire, game over")

    elif choice2 == "B" or choice2 == "b":

      print("Eaten by beasts, game over")

    elif choice2 == "Y" or choice2 == "y":

      print("You win!!")

    else:

      print("Game over")
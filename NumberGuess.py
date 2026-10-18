# Number guessing game
import random
Rounds_Played = 0
Start = input("Hello would you like to play the number guessing game? (Y/N)  ").upper()
while Start == "Y":
    Comp_Number = random.randint(1, 100)
    Player_Guess = int(input("Please guess the random number between 1-100  "))
    while (Player_Guess != Comp_Number):
        if (Player_Guess > Comp_Number):
            print("Lower")
            Player_Guess = int(input("Keep Guessing:  "))
        elif (Player_Guess < Comp_Number):
            print("Higher")
            Player_Guess = int(input("Keep Guessing:  "))
    print("You did it! the Correct number was: " + str(Comp_Number))
    Start = input("Would you like to keep playing? (Y/N) ").upper

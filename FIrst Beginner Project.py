# Rock, Paper, Scissors Game
# making computer
import random
Options = [["You Tied", "You Lost", "You Won"],
           ["You Won", "You Tied", "You Lost"],
           ["You Lost", "You Won", "You Tied"]]
#Game_Run = 1
while True:
    Start = input("Hello would you like to play Rock, Paper, Scissors?(Y/N)  ")
    while Start == "Y":
        Comp_Choice = random.randint(1, 3)
        Player_Choice = int(input("Ok choose: Rock = 1, Paper = 2, Scissors = 3  "))
        Game_decision = Options[Player_Choice - 1][Comp_Choice - 1]
        print(str(Game_decision) + " The computer chose " + str(Comp_Choice))
        Running = input("Would you like to keep playing? (Y/N)")
        if Running == "N":
            Start = "N"
    else:
        break


    


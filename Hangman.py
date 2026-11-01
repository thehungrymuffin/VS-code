#Hangman game
# list of possible words
import random
words = ["shark", "gamer", "gumpo", "obtuse"]

def round():
    current_word = list()
    chosen_word = list(words[random.randint(0, len(words) - 1)])
    discarded_letters = []
    lives = 10
    game_condition = True

    #Testing
    print(chosen_word)

    print("The word chosen is: ")
    for i in range(0, len(chosen_word)):
        current_word.append("_")
        print("_", end = " ")

    player_letter = input("\nwould you like to guess the first letter? ").lower()

    while (current_word != chosen_word and game_condition == True):
        word_condition = False
        if (len(player_letter) != 1):
            player_letter = input("You need to pick only 1 letter for the guess try again: ")
        for i in range(0 , len(chosen_word)):
            if player_letter == chosen_word[i]:
                current_word[i] = player_letter
                word_condition = True
        if (word_condition == True):
            print("Here are your discarded letters so far: " + str(discarded_letters))
            player_letter = input("\nGood job the current word is " + " ".join(current_word) + " keep guessing: ").lower()
        else:
            discarded_letters.append(player_letter)
            print("Here are your discarded letters so far: " + str(discarded_letters))
            player_letter = input("Sorry that word was incoorect keep guessing: ").lower()
            lives -= 1
            if lives == 0:
                game_condition = False
                break
    if game_condition == True:
        print("Wow you did it the word was" + str(chosen_word))
    else:
        print("You failed all your lives!")

            

    

        


intro = input("Hello would you like to play Hangman? (Y/N)  ").upper()
if intro == "Y":
    round()
else:
    print("Thanks for Playing!")
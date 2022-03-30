# Libraries

import colorama
from colorama import init, Fore, Back, Style # To output the letters colorful.
from colored_text import ColoredText
from word_list import valid_words
import random 

# Program

control_flag = True
while control_flag:
    print(Back.CYAN + Fore.BLACK + "Do you want to start a new game? (y/n)" + Style.RESET_ALL)
    play_or_quit = input().lower()
        
    if play_or_quit == "n":
        print("We hope to see you soon again!") 
        control_flag = False

    elif play_or_quit != "y" and play_or_quit != "n":
        print("Please enter a valid selection 'y' or 'n'.")
        
    elif play_or_quit == "y":
        credit = 6 
        secret_word = random.choice(valid_words)
        print("Welcome to the Wordle game! \nPlease enter only 5 letter words.")

        guessed_word = ""
        while secret_word != guessed_word or credit > 0:
            guessed_word = input().lower()
                
            if guessed_word not in valid_words:
                print(f"Word not found. You still have {credit} attempts.")
        
            else:
                text = ""
                for i in range(len(secret_word)):
                    if guessed_word[i] == secret_word[i]:
                        text = text + str(ColoredText(guessed_word[i]).in_spot())
                    elif guessed_word[i] in secret_word:
                        text = text + str(ColoredText(guessed_word[i]).not_in_spot())
                    else:
                        text = text + str(ColoredText(guessed_word[i]).not_in_word())
    
                if guessed_word == secret_word:
                    print("",end="\n")
                    print("*"*19)
                    print("*"," "*15,"*")
                    print("*","Congratulations","*")
                    print("*"," "*15,"*")
                    print("*"*19)   
                    # Print the correct word.
                    print(f"You found the correct word '{secret_word.upper()}'!")
                    break
            
                else:
                    credit = credit - 1 
                    print(f"\t**You have {credit} attempts left.",end= "||||")
        
                    if credit == 0:                     
                        print("\n")
                        print("*"*13)
                        print("*"," "*9,"*")
                        print("*","Game over","*")
                        print("*"," "*9,"*")
                        print("*"*13)
                        # Print the correct word.
                        print(f"The secret word was '{secret_word.upper()}'.")
                        break

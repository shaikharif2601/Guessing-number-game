# This is a Number Guessing Game.

number  = 12
"""
    Player have to guess this number. In 3 chance
"""

no_of_guess = 0
print("\n")
print("**********************************|Welcome to Number Guessing Game.|**************************************")
print("\n")
print("\n\t\t\tIn This you have 3 chance.You have to guess a correct number .")
print("\n")
print("\n************************************************************************************************************")


while ( no_of_guess < 3 ):                                  #create a while loop for of game
    no_of_guess = no_of_guess + 1                           #this line will add the no of chance ever time we play till 3 chance

    guess_a_number = int(input("\n\tGuess a number from 1 to 20 :-\t"))

    if guess_a_number == 12:
        print("\n")
        print("\n*********************************|Congratulation|*************************************************")
        print("\n") 2
        print("\n***************************You guess a correct number******************************************")
        break

    elif guess_a_number < number:
        print("\n")
        print("\tYou've enter a smaller number, Please enter a higher number")
        print("\n")
        print(f"\tYou have {3 - no_of_guess} left.")

        continue

    elif guess_a_number > number:
        print("\n")
        print("\tYou've enter a higher number, please enter a smaller number")
        print("\n")
        print(f"\tYou have {3 - no_of_guess} chances left.")

    else:
        pass

print(f"\n\t\t {no_of_guess} :- no of chance you took to finish this game ")
print("\n")

if (no_of_guess > 3):
    print("\n")
    print("*****************************************|GAME OVER|*************************************")
    print("\n")
    print('\n\tYou took more than 3 chacnce.')
    print("\n")


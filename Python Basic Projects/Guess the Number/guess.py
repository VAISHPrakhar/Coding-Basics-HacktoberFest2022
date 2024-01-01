#guess the number game
import random

def guess_the_number():
    play_again = "yes"
    
    while play_again.lower() == "yes":
        number = random.randint(1, 100)
        guess = int(input("Guess the number between 1 and 100: "))
        
        while guess != number:
            if guess < number:
                print("Guess higher")
            else:
                print("Guess lower")
            guess = int(input("Try again: "))
        
        print("You guessed it! The number was", number)
        play_again = input("Do you want to play again? (yes/no): ")

guess_the_number()

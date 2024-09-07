import random

# array of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# have the computer choose a random number.

choice = random.choice(numbers)
# ask the user for input; his or her guess.
# if statements to check if the users input was true(guess was right) or not(guess was wrong)
lives = 3
gameOver = False
print(f"You have {lives} lives.")
while gameOver == False:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == choice:
        print("YAY")
        gameOver = True
    else:
        if lives == 0:
            print("Game Over")
            gameOver = True
        elif guess > choice:
            lives -= 1
            print(f"Your guess was too high. you have {lives} lives left")
        elif guess < choice:
            lives -= 1
            print(f"Your guess was too low. you have {lives} lives left")

# if its wrong tell the user if his or her input is > or < then



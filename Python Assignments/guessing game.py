from random import randint

number = randint (1,10)

guess = 0


while(guess != number):

    print("Guess a number between 1 to 10")
    guess = int(input())

    print(guess)

    if guess != number:
        print("Incorrect")

    else:
        print("Correct")


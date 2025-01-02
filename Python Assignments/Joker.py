'''This program, Joke Machine, was created by Shrut and Darius and in this program you will be asked 5 jokes in a certain difficulty level (easy, hard and impossible). The user can pick what level of difficulty the joke will be or the computer can generate a difficulty level for them. After the user guesses the punchline the computer will tell them if they are correct or incorrect. The score, with a corresponding message will be displayed after the program is finished
DATE STARTED: 11/22/2023
DATE FINISHED: 11/23/2023'''

from time import sleep
from random import randint
import pgzrun #This will automatically open. Please ignore the tab when it opens, as when it opens it will be empty, but when you finish the game, it will output its image and character after you finish your game.

background_loose = Actor("sad-image")
background_win = Actor("happy-image")
winner = Actor("happy-apple")
loser = Actor("troll-face")


#Welcome user to the program
print("Welcome to joke game")

#Set variable score to 0
score = 0

#Prompt user for their name
print("What is your name? ")
name = input()

score = 0

#Welcome the user to the program
print("Hello", name, "- in this game you are to guess the ending of the joke. You will choose the difficulty next. I will then ask you a joke and you must guess the punchline corresponding to the joke. Please wait...")

#Let them comprehend the message
sleep(5)

#Prompt them to pick their difficulty
print("Let's begin! Choose between (1) or (2)")

#Initiate try and except to make sure value is a integer
try:
    pick = int(input())
except ValueError:
    print("You must enter a number")
    pick = int(input())

#Check if the pick is 1 and prompt user to enter their difficulty
if pick == 1:
    print("You are doing hard mode. Get ready!")
    sleep (3)

    print("GUESS THE PUNCHLINE: What should I do when I loose a electron")
    guess1 = input().lower()

    #check if they guessed right
    if guess1 == "keep a ion them":
        print("CORRECT STARTING STRONG (1/5)")
        score = score + 1

    #check if they guessed right with different form (only 0.5 with this)
    elif guess1 == "ion":
        print("CORRECT but only half marks because it was not fully said (1/5)")
        score = score + 0.5

    #if both booleans false, run else
    else:
        print("Sorry that does not ring a bell! Lets try again? (1/5)")
        print("The correct answer is keep a ion them")

    sleep(1)
    print("STARTING NEXT ONE GET READY...")
    sleep(2)

    #prompt user for the punchline
    print("GUESS THE PUNCHLINE: What did 0 say to 8")
    guess2 = input().lower()

    #check if they are correct
    if guess2 == "nice belt":
        print("CORRECT!(2/5)")
        score = score + 1

    #if both booleans false, run else
    else:
        print("Sorry that does not ring a bell! Lets try again? (2/5)")
        print("The correct answer is nice belt")

    sleep(1)
    print("STARTING NEXT ONE GET READY...")
    sleep(2)

    #prompt user for punchline
    print("GUESS THE PUNCHLINE: What is red and hard to eat?")
    guess3 = input().lower()

    #check if they guessed correct
    if guess3 == "brick":
        print("CORRECT!(3/5)")
        score = score + 1
    #check if they guessed correct different style
    elif guess3 == "a brick":
        print("CORRECT!(3/5)")
        score = score + 1

    #if both booleans false, run else
    else:
        print("Sorry that does not ring a bell! Lets try again? (3/5)")
        print("The correct answer is a brick")

    sleep(1)
    print("STARTING NEXT ONE GET READY...")
    sleep(2)

    #prompt user to guess punchline
    print("GUESS THE PUNCHLINE: What type of cheese is not yours?")
    guess4 = input().upper()

    #check if the guess is correct
    if guess4 == "NACHO CHEESE":
        print("CORRECT!(4/5)")
        score = score + 1

    #if both booleans false, run else
    else:
        print("Sorry that does not ring a bell! Lets try again? (4/5)")
        print("The correct answer is NACHO CHEESE HAHA")

    sleep(1)
    print("STARTING NEXT ONE GET READY...")
    sleep(2)

    #prompt user to guess punchline
    print("(LAST ONE) GUESS THE PUNCHLINE: Why do computers overheat")
    guess5 = input().lower()

    #check if they are correct
    if guess5 == "they need to vent":
        print("CORRECT!(5/5)")
        score = score + 1

    #if both booleans false, run else
    else:
        print("Sorry that does not ring a bell! Lets see your final score! (5/5)")
        print("The correct answer is they need to vent")

    sleep(2)

    #print user final score
    print("YOUR FINAL SCORE IS ",score)

    if score >= 3:
        print ("You win! You belong in a circus.")
        music.play ("amazing")
        def place_background_loose():
            background_loose.x = randint (50,500)
            background_loose.y = randint (50,500)
        def place_loser():
            winner.x = randint (50,500)
            winner.y = randint (50,500)
        pgzrun.go()
    else:
        print ("You lost!")
        def place_background_loose():
            background_loose.x = randint (50,500)
            background_loose.y = randint (50,500)
        def place_loser():
            winner.x = randint (50,500)
            winner.y = randint (50,500)
        pgzrun.go()


#Pick a random number if number picked is 2
elif pick == 2:
    hard = randint (1,100)
    print("You are doing easy mode. Get ready!")
    sleep (3)
    print("Are you ready to start", name, "?")
    ready = input().lower()

    if ready == "yes":
        print("Starting now")
        sleep(1)
        print("Loading EASY difficulty questions...")
        sleep(1)

    elif ready == "no":
        print("Take your time", name, "There is some time to wait.")
        sleep(5)
        print("Loading EASY difficulty questions...")
        sleep(1)

    else:
        print("I am not sure what you mean. Starting soon anyways... ")
        sleep(2)
        print("Loading EASY difficulty questions...")
        sleep(1)

    #prompt user to guess punchline
    print("GUESS THE PUNCHLINE: What is brown and sticky")
    guess1 = input().lower()

    #check if it is correct
    if guess1 == "a stick":
        print("CORRECT STARTING STRONG (1/5)")
        score = score + 1

    #check if it correct with different spelling
    elif guess1 == "stick":
        print("CORRECT STARTING STRONG" (1/5))
        score = score + 1

    #if both booleans false, run else
    else:
        print("Sorry that does not ring a bell! Lets try again? (1/5)")
        print("The correct answer is a stick!!")

    sleep(1)
    print("STARTING NEXT ONE GET READY...")
    sleep(2)

    #prompt user to guess punchline
    print("GUESS THE PUNCHLINE: What would be bears without bees")
    guess2 = input().lower()

    #check if the guess is right
    if guess2 == "ears":
        print("CORRECT!(2/5)")
        score = score + 1

    #if both booleans false, run else
    else:
        print("Sorry that does not ring a bell! Lets try again? (2/5)")
        print("The correct answer is ears!")

    sleep(1)
    print("STARTING NEXT ONE GET READY...")
    sleep(2)

    #prompt user to guess punchline
    print("GUESS THE PUNCHLINE: What did the Triangle say to the circle")
    guess3 = input().lower()

    #check if they are correct
    if guess3 == "you are pointless":
        print("CORRECT!(3/5)")
        score = score + 1

    #check if they are correct but different version
    elif guess3 == "you're pointless":
        print("CORRECT!3/5)")
        score = score + 1

    #if both booleans false, run else
    else:
        print("Sorry that does not ring a bell! Lets try again? (3/5)")
        print("The correct answer is you are pointless")

    sleep(1)
    print("STARTING NEXT ONE GET READY...")
    sleep(2)

    #prompt user to guess punchline
    print("GUESS THE PUNCHLINE: What do you call a fish without a eye")
    guess4 = input().lower()

    #check if guess is correct
    if guess4 == "fsh":
        print("CORRECT!(4/5)")
        score = score + 1

    #if both booleans false, run else
    else:
        print("Sorry that does not ring a bell! Lets try again? (4/5)")
        print("The correct answer was: A fsh")

    sleep(1)
    print("STARTING NEXT ONE GET READY...")
    sleep(2)

    #prompt user to guess punchline
    print("(LAST ONE) GUESS THE PUNCHLINE: What do you call a pig that does karate")
    guess5 = input().lower()

    #check if they are correct
    if guess5 == "a pork chop":
        print("CORRECT!(5/5)")
        score = score + 1

    #check if they are correct but in a different version
    elif guess5 == "pork chop":
        print("CORRECT!(5/5)")
        score = score + 1

    #if both booleans false, run else
    else:
        print("Sorry that does not ring a bell! Lets see your final score! (5/5)")
        print("The correct answer is a pork chop")

    sleep(2)

    #print final score
    print("YOUR FINAL SCORE IS ",score)

    #check what the score is and print a message according to it

    if score >= 3:
        print ("You win! You belong in a circus.")
        music.play("amazing")
        def place_background_loose():
            background_loose.x = randint (50,500)
            background_loose.y = randint (50,500)
        def place_loser():
            winner.x = randint (50,500)
            winner.y = randint (50,500)
        pgzrun.go()
    else:
        print ("You lost!")
        def place_background_loose():
            background_loose.x = randint (50,500)
            background_loose.y = randint (50,500)
        def place_loser():
            winner.x = randint (50,500)
            winner.y = randint (50,500)
        pgzrun.go()

#If they enter num that is not 1 or 2
else:
    print("This was not a valid number. You will not be able to play.")
    sleep (2)






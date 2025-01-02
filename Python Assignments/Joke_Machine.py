'''This program, Joke Machine was created by Shrut and Darius and in this program you will be asked 5 jokes in a certain difficulty level (Easy, Hard and impossible). The user can pick what level difficulty the joke will be or the computer can generate a difficulty level for them. After the user guesses the punchline the computer will tell them if they are correct or incorrect. The score, with a corresponding message will be displayed after the program is finished
DATE STARTED: 11/22/2023
DATE FINISHED: 11/23/2023'''

from time import sleep
from random import randint

#Welcome user to the program
print("Welcome to joke game")

#Set variable score to 0
score = 0

#Prompt user for their name
print("What is your name? ")
name = input()

#Welcome the user to the program
print("Hello", name, "In this game I will ask you to choose your difficulty. I will then ask you a joke and you must guess the punchline corresponding to the joke")

#Let them comprehend the message
sleep(3)

#Prompt them to pick their difficulty
print("Let's begin! Do you want to pick your own difficulty (1) or I pick (2)")

#Initiate try and except to make sure value is a integer
try:
    pick = int(input())
except ValueError:
    print("You must enter a number")
    pick = int(input())

#Check if the pick is 1 and prompt user to enter their difficulty
if pick == 1:
    print("What difficulty do you want? from 1-30 (Easy) 31-60 (Hard) 61 - 100 (Impossible).")

    #Use try, except method to initaite a validation check and make sure number is a whole number
    try:
        hard = int(input())
    except ValueError:
        print("You must enter a number")
        hard = int(input())

#Pick a random number if number picked is 2
elif pick == 2:
    hard = randint (1,100)
    print("I generated you to be", hard, "difficulty")

#If they enter num that is not 1 or 2
else:
    print("This was not a valid number")


sleep(2)

#if the hard level is over 60 that means they want it impossible
if hard> 60:
    print("WOW", name, "Seems like you want it IMPOSSIBLE DIFFICULTY")

    #Give user time to prepare
    sleep(2)

    #Wait for this to be ready
    print("Are you ready to start", name, "?")
    ready = input().lower()

    #Inform user the program is starting regardless of what they pick
    if ready == "yes":
        print("Good Job starting now")
        sleep(1)
        print("Loading IMPOSSIBLE difficulty questions...")
        sleep(1)


    elif ready == "no":
        print("Take your time", name, "I can give you some time to wait")
        sleep(5)
        print("Loading IMPOSSIBLE difficulty questions...")
        sleep(1)

    else:
        print("I am not sure what you mean. Starting soon anyways... ")
        sleep(2)
        print("Loading IMPOSSIBLE difficulty questions...")
        sleep(1)

    #Prompt user to guess punchline
    print("GUESS THE PUNCHLINE: How did the hipster burn his tongue")
    guess1 = input().lower()

    #Check if they are correct
    if guess1 == "he drank his coffee before it was cool":
        print("CORRECT STARTING STRONG (1/5)")
        score = score + 1

    #if both booleans false, run else
    else:
        print("Sorry that does not ring a bell! Lets try again? (1/5)")
        print("The correct answer is he drank his coffee before it was cool")

    sleep(2)
    print("STARTING NEXT ONE GET READY...")
    sleep(2)

    #Prompt user to guess punchline
    print("GUESS THE PUNCHLINE: What did 50 do when he was hungry ")
    guess2 = input().lower()

    #check if they are correct
    if guess2 == "58":
        print("CORRECT!(2/5)")
        score = score + 1

    #if both booleans false, run else
    else:
        print("Sorry that does not ring a bell! Lets try again? (2/5)")
        print("The correct answer is 58")

    sleep(2)
    print("STARTING NEXT ONE GET READY...")
    sleep(2)

    #Prompt user to guess punchline
    print("GUESS THE PUNCHLINE: How did the barber win his race?")
    guess3 = input().lower()

    #check if they are correct
    if guess3 == "he knew a shortcut":
        print("CORRECT!(3/5)")
        score = score + 1

    #if both booleans false, run else
    else:
        print("Sorry that does not ring a bell! Lets try again? (3/5)")
        print("The correct answer is he knew a shortcut")

    sleep(2)
    print("STARTING NEXT ONE GET READY...")
    sleep(2)

    #Prompt user to guess punchline
    print("GUESS THE PUNCHLINE: Why did the belt go to jail?")
    guess4 = input().lower()

    #check if they are correct
    if guess4 == "because it held up a pair of jeans":
        print("CORRECT!(4/5)")
        score = score + 1

    #check if they are correct (different speech)
    elif guess4 == "it held up a pair of jeans":
        print("CORRECT!(4/5)")
        score = score + 1

    #if both booleans false, run else
    else:
        print("Sorry that does not ring a bell! Lets try again? (4/5)")
        print("The correct answer is (because) it held up a pair of jeans")

    sleep(2)
    print("STARTING NEXT ONE GET READY...")
    sleep(2)

    #Prompt user to guess punchline
    print("(LAST ONE) GUESS THE PUNCHLINE: How do you tell the difference between a bull and a cow")
    guess5 = input().lower()

    #check if they are correct
    if guess5 == "it is either one or the udder":
        print("CORRECT!(5/5)")
        score = score + 1

    #if both booleans false, run else
    else:
        print("Sorry that does not ring a bell! Lets see your final score! (5/5)")
        print("The correct answer is it is either one or the udder")

    sleep(2)
    #print user final score
    print("YOUR FINAL SCORE IS ",score)

    #check what the score is and print the corresponding message
    if score ==0:
        print("I am very dissapointed", name)
    elif score == 1:
        print("Need some more practising ",name)
    elif score ==2:
        print("Keep working hard!")
    elif score ==3:
        print("Not bad!", name)
    elif score ==4:
        print("Wow you must be a good joker")
    elif score ==5:
        print("You are a clown haha", name)



#if the difficulty is not over 60, check if it is over 30 to see if they wanted hard mode
elif hard > 30:
    print("It seems that your difficulty will be HARD", name, "do not let the jokes fool you")

    #prepare the user to start
    print("Are you ready to start", name, "?")
    ready = input().lower()

    if ready == "yes":
        print("Good Job starting now")
        sleep(1)
        print("Loading HARD difficulty questions...")
        sleep(1)

    elif ready == "no":
        print("Take your time", name, "I can give you some time to wait")
        sleep(5)
        print("Loading HARD difficulty questions...")
        sleep(1)

    else:
        print("I am not sure what you mean. Starting soon anyways... ")
        sleep(2)
        print("Loading HARD difficulty questions...")
        sleep(1)

    #prompt user to guess the punchline
    print("GUESS THE PUNCHLINE: What should I do when I loose a electron")
    guess1 = input().lower()

    #check if they guessed right
    if guess1 == "keep a ion them":
        print("CORRECT STARTING STRONG (1/5)")
        score = score + 1

    #check if they guessed right with different form (only 0.5 with this)
    elif guess1 == "ion":
        print("CORRECT but only half marks because it was not fully said" (1/5))
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
        print("CORRECT!3/5)")
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

    #print the corresponding message to their score
    if score ==0:
        print("I am very dissapointed", name)
    elif score == 1:
        print("Need some more practising ",name)
    elif score ==2:
        print("Keep working hard!")
    elif score ==3:
        print("Not bad!", name)
    elif score ==4:
        print("Wow you must be a good joker")
    elif score ==5:
        print("You are a clown haha", name)


#if the hard level is not over 30 check if it is over than 0, so it will be easy level
elif hard> 0:
    print("It seems that your difficulty will be easy", name, "you better do good and make me proud")

    #ask user if they are ready to start and print a message based on their response
    print("Are you ready to start", name, "?")
    ready = input().lower()

    if ready == "yes":
        print("Good Job starting now")
        sleep(1)
        print("Loading EASY difficulty questions...")
        sleep(1)

    elif ready == "no":
        print("Take your time", name, "I can give you some time to wait")
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
        print("A fsh")

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
    if score ==0:
        print("I am very dissapointed", name)
    elif score == 1:
        print("Need some more practising ",name)
    elif score ==2:
        print("Keep working hard!")
    elif score ==3:
        print("Not bad!", name)
    elif score ==4:
        print("Wow you must be a good joker")
    elif score ==5:
        print("You are a clown haha", name)

#if the user entered any other number (negative) then this else statement will run
else:
    print("Please enter a positive number", name, "!")


from time import sleep
from random import randint

#Welcome user to the program
print("Welcome to joke game")

score = 0

print("What is your name? ")
name = input()

print("Hello", name, "In this game I will ask you to choose your difficulty. I will then ask you a joke and you must guess the punchline corresponding to the joke")

sleep(3)

print("Let's begin! Do you want to pick your own difficulty (1) or I pick (2)")


try:
    pick = int(input())
except ValueError:
    print("You must enter a number")
    pick = int(input())

if pick == 1:
    print("What difficulty do you want? from 1-30 (Easy) 31-60 (Hard) 61 - 100 (Impossible).")

    #Use try, except method to initaite a validation check and make sure number is a whole number
    try:
        hard = int(input())
    except ValueError:
        print("You must enter a number")
        hard = int(input())




elif pick == 2:
    hard = randint (1,100)
    print("I generated you to be", hard, "difficulty")

else:
    print("This was not a valid number")


sleep(2)

if hard> 60:
    print("WOW", name, "Seems like you want it IMPOSSIBLE DIFFICULTY")

    sleep(2)

    print("Are you ready to start", name, "?")
    ready = input().lower()

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

    print("GUESS THE PUNCHLINE: How did the hipster burn his tongue")
    guess1 = input().lower()

    if guess1 == "he drank his coffee before it was cool":
        print("CORRECT STARTING STRONG (1/5)")
        score = score + 1

    else:
        print("Sorry that does not ring a bell! Lets try again? (1/5)")

    sleep(1)
    print("STARTING NEXT ONE GET READY...")
    sleep(2)

    print("GUESS THE PUNCHLINE: What did 50 do when he was hungry ")
    guess2 = input().lower()

    if guess2 == "58":
        print("CORRECT!(2/5)")
        score = score + 1

    else:
        print("Sorry that does not ring a bell! Lets try again? (2/5)")

    sleep(1)
    print("STARTING NEXT ONE GET READY...")
    sleep(2)

    print("GUESS THE PUNCHLINE: How did the barber win his race?")
    guess3 = input().lower()

    if guess3 == "he knew a shortcut":
        print("CORRECT!(3/5)")
        score = score + 1

    else:
        print("Sorry that does not ring a bell! Lets try again? (3/5)")

    sleep(1)
    print("STARTING NEXT ONE GET READY...")
    sleep(2)

    print("GUESS THE PUNCHLINE: Why did the belt go to jail?")
    guess4 = input().lower()

    if guess4 == "because it held up a pair of jeans":
        print("CORRECT!(4/5)")
        score = score + 1

    elif guess4 == "it held up a pair of jeans":
        print("CORRECT!(4/5)")
        score = score + 1

    else:
        print("Sorry that does not ring a bell! Lets try again? (4/5)")

    sleep(1)
    print("STARTING NEXT ONE GET READY...")
    sleep(2)

    print("(LAST ONE) GUESS THE PUNCHLINE: How do you tell the difference between a bull and a cow")
    guess5 = input().lower()

    if guess5 == "it is either one or the udder":
        print("CORRECT!(5/5)")
        score = score + 1

    else:
        print("Sorry that does not ring a bell! Lets see your final score! (5/5)")

    sleep(2)

    print("YOUR FINAL SCORE IS ",score)

    if score == 1:
        print("Need some more practising ",name)
    if score ==2:
        print("Keep working hard!")
    if score ==3:
        print("Not bad!", name)
    if score ==4:
        print("Wow you must be a good joker")
    if score ==5:
        print("You are a clown haha", name)




elif hard > 30:
    print("It seems that your difficulty will be HARD", name, "do not let the jokes fool you")


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

    print("GUESS THE PUNCHLINE: What should I do when I loose a electron")
    guess1 = input().lower()

    if guess1 == "keep a ion then":
        print("CORRECT STARTING STRONG (1/5)")
        score = score + 1

    elif guess1 == "ion":
        print("CORRECT but only half marks because it was not fully said" (1/5))
        score = score + 0.5

    else:
        print("Sorry that does not ring a bell! Lets try again? (1/5)")

    sleep(1)
    print("STARTING NEXT ONE GET READY...")
    sleep(2)

    print("GUESS THE PUNCHLINE: What did 0 say to 8")
    guess2 = input().lower()

    if guess2 == "nice belt":
        print("CORRECT!(2/5)")
        score = score + 1

    else:
        print("Sorry that does not ring a bell! Lets try again? (2/5)")

    sleep(1)
    print("STARTING NEXT ONE GET READY...")
    sleep(2)

    print("GUESS THE PUNCHLINE: What is red and hard to eat?")
    guess3 = input().lower()

    if guess3 == "brick":
        print("CORRECT!(3/5)")
        score = score + 1

    if guess3 == "a brick":
        print("CORRECT!3/5)")
        score = score + 1

    else:
        print("Sorry that does not ring a bell! Lets try again? (3/5)")

    sleep(1)
    print("STARTING NEXT ONE GET READY...")
    sleep(2)

    print("GUESS THE PUNCHLINE: What type of cheese is not yours?")
    guess4 = input().upper()

    if guess4 == "NACHO CHEESE":
        print("CORRECT!(4/5)")
        score = score + 1

    else:
        print("Sorry that does not ring a bell! Lets try again? (4/5)")

    sleep(1)
    print("STARTING NEXT ONE GET READY...")
    sleep(2)

    print("(LAST ONE) GUESS THE PUNCHLINE: Why do computers overheat")
    guess5 = input().lower()

    if guess5 == "they need to vent":
        print("CORRECT!(5/5)")
        score = score + 1

    else:
        print("Sorry that does not ring a bell! Lets see your final score! (5/5)")

    sleep(2)

    print("YOUR FINAL SCORE IS ",score)

    if score == 1:
        print("Need some more practising ",name)
    if score ==2:
        print("Keep working hard!")
    if score ==3:
        print("Not bad!", name)
    if score ==4:
        print("Wow you must be a good joker")
    if score ==5:
        print("You are a clown haha", name)



elif hard> 0:
    print("It seems that your difficulty will be easy", name, "you better do good and make me proud")


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

    print("GUESS THE PUNCHLINE: What is brown and sticky")
    guess1 = input().lower()

    if guess1 == "a stick":
        print("CORRECT STARTING STRONG (1/5)")
        score = score + 1

    elif guess1 == "stick":
        print("CORRECT STARTING STRONG" (1/5))
        score = score + 1

    else:
        print("Sorry that does not ring a bell! Lets try again? (1/5)")

    sleep(1)
    print("STARTING NEXT ONE GET READY...")
    sleep(2)

    print("GUESS THE PUNCHLINE: What would be bears without bees")
    guess2 = input().lower()

    if guess2 == "ears":
        print("CORRECT!(2/5)")
        score = score + 1

    else:
        print("Sorry that does not ring a bell! Lets try again? (2/5)")

    sleep(1)
    print("STARTING NEXT ONE GET READY...")
    sleep(2)

    print("GUESS THE PUNCHLINE: What did the Triangle say to the circle")
    guess3 = input().lower()

    if guess3 == "you are pointless":
        print("CORRECT!(3/5)")
        score = score + 1

    if guess3 == "you're pointless":
        print("CORRECT!3/5)")
        score = score + 1

    else:
        print("Sorry that does not ring a bell! Lets try again? (3/5)")

    sleep(1)
    print("STARTING NEXT ONE GET READY...")
    sleep(2)

    print("GUESS THE PUNCHLINE: What do you call a fish without a eye")
    guess4 = input().lower()

    if guess4 == "fsh":
        print("CORRECT!(4/5)")
        score = score + 1

    else:
        print("Sorry that does not ring a bell! Lets try again? (4/5)")

    sleep(1)
    print("STARTING NEXT ONE GET READY...")
    sleep(2)

    print("(LAST ONE) GUESS THE PUNCHLINE: What do you call a pig that does karate")
    guess5 = input().lower()

    if guess5 == "a pork chop":
        print("CORRECT!(5/5)")
        score = score + 1

    if guess5 == "pork chop":
        print("CORRECT!5/5)")
        score = score + 1

    else:
        print("Sorry that does not ring a bell! Lets see your final score! (5/5)")

    sleep(2)

    print("YOUR FINAL SCORE IS ",score)

    if score == 1:
        print("Need some more practising ",name)
    if score ==2:
        print("Keep working hard!")
    if score ==3:
        print("Not bad!", name)
    if score ==4:
        print("Wow you must be a good joker")
    if score ==5:
        print("You are a clown haha", name)


else:
    print("Please enter a positive number", name, "!")


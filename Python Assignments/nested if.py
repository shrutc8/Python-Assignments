
#Prompt user to pick one
print("Pick either Carrot, Broccoli, Peas or Sweetcorn")

#Tell user that you will guess there choice
print("I will attempt to guess your choice")

#Ask user if vegetable is green
print("is the vegetable green? Y/N")

answer = input().lower()

#Check if answer is no
if answer == "n":

    #Ask a follow up question
   print("Is the vegetable orange? Y/N" )
   answer2 = input().lower()

    #if answer is yes it must be a carrot
   if answer2 == "y":

       print("It must be a carrot!")

    #if it is not a carrot then it is sweet corn
   else:
        print("It must be a sweet corn")

#check if answer yes
if answer == "y":

    #is the vegetable shaped like a tree
    print("Is the vegetable shaped like a tree Y/N")
    answer3 = input().lower()

    #check if answer is yes for that so broccoli
    if answer3 == "y":
        print("It must be a broccoli ")

    #check if it not
    if answer3 == "n":
        print("It is peas!")


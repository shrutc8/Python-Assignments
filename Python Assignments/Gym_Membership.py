from time import sleep

'''This program will get personal information from the user, ask the user how many months they would like to pay for then calculate the total it will cost. '''


#Welcome user to the program
print("Welcome to gym membership")

#Wait 2 secounds for user to understand
sleep (2)

#Prompt the user to enter their name
print("What is your name? ")
name = input()

#Prompt the user to enter their age
print("What is your age")

#Use try, except method to initaite a validation check and make sure number is a whole number
try:
    age = int(input())
except ValueError:
    print("You must enter a number")
    age = int(input())

#Inform the user that the process is almost complete
print ("Thank you for this information, we are almost complete")
sleep(1)

#Prompt user to enter adress
print("Please enter your address to check for our radius compatibility")
address = input()

#Check adress radius and wait some time to check
print("Checking address radius <--->")
sleep(2)

#Inform the user their adress is infact in range
print("Thank you", address, "is in range")
sleep(1)

#Prompt the user to enter their email adress to stay updated on pricings
print("Please enter your email address for us to keep you updated on our pricings")
email = input()


#Ask user if they would like to learn about pricing plans
print("Welcome", age, "year old", name, "Press enter to learn about pricing plans")
enter = input()

#Print pricing plans monthly
print("Our prices start at Monthly: $35 + tax if prices do improve we will email you at", email, "Thank you" )

#Wait 2 secound for user to comprehend information
sleep(2)

#Prompt the user to enter how many months they will pay for
print("How many months will you join us for? ")

#Use try, except method to initaite a validation check and make sure number is a whole number
try:
    time = int(input())
except ValueError:
    print("You must enter a number")
    time= int(input())

#Calculate the total including tax
total = (time * 35) * 1.13

#Print how much it will cost to the user
print("For", time, "months it will cost", total, "including tax")

#Ask the user for their method of payment
print("Would you like to pay with Credit Card or Debit Card ")
payment_method = input()

#Tell the user to enter their pin
print("Please enter your pin")

#Create validation check to ensure the pin is a number
try:
    pin = int (input())
except ValueError:
    print("PIN IS NOT VALID")
    pin = int (input())

#Thank the user for their business
print("Thank you for your business, we hope to see you for " ,time, "months", "Enjoy your day",name,"!")
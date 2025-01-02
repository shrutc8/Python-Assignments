                         '''This program will ask the user if they are eligible for youth discount'''

#Prompt user to enter num
print("Enter in age: ")

#Create validation check to make sure they input correct num
try:
    age = int(input())
except ValueError:
    print("You must enter a number")
    age = int(input())

#Check if age between 18 and 30
if age<= 30 and age >= 18:
    print("You are elible for youth discount")

#Tell user they are not eligible
else:
    print("You are not eligible for youth discount")
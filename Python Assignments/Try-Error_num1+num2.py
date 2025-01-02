print("Enter a number")

try:
    number = int(input())
except ValueError:
    print("You must enter a number")
    number= int(input())

print("Enter a number")

try:
    number1 = int(input())
except ValueError:
    print("You must enter a number")
    number1= int(input())
print(number + number1)

print("Enter in times table number")

try:
    times_table = int(input())
except ValueError:
    print("You must enter a number")
    times_table = int(input())

print("Enter maximum value for this")

try:
    max = int(input())
except ValueError:
    print("You must enter a number")
    max = int(input())

answer = 0

print(f"Here is the {times_table} times table")

for x in range(1,max):
    answer = x * times_table
    print(f"{x} times {times_table} is {answer}")

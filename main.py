# List of numbers
numbers = [5, 20, 30, 30, 50]

# Get value to delete from user
delval = int(input('Enter the deletion value: '))

# Remove value from list
try:
    for i in range(2):
        delIndex = numbers.index(delval)
        del numbers[delIndex]
except ValueError:
    numbers.clear()

# Print updated list
print (numbers)

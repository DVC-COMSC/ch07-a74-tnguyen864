# List of numbers
numbers = [5, 20, 30, 30, 50]

# Get value to delete from user
delval = int(input('Enter the deletion value: '))

# Remove value from list
occur = numbers.count(delval)
if occur > 0:
    for i in range(occur):
        numbers.remove(delval)
else:
    numbers.clear()

# Print updated list
print (numbers)

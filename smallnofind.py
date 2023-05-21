# Take 10 integer inputs from the user
numbers = []
for i in range(5):
    number = int(input("Enter number {}: ".format(i+1)))
    numbers.append(number)

# Find the smallest and second smallest numbers
smallest = min(numbers)
second_smallest = min(num for num in numbers if num != smallest)

# Output the second smallest number
print("The second smallest number is:", second_smallest)

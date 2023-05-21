# Take 10 integer inputs from the user
numbers = []
for i in range(5):
    number = int(input("Enter number {}: ".format(i+1)))
    numbers.append(number)

# Find the largest and second largest numbers
largest = max(numbers)
second_largest = max(num for num in numbers if num != largest)

# Output the second largest number
print("The second largest number is:", second_largest)

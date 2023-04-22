print("Welcome to the Love Calculator!")
name1 = input("Please enter your name: ")
name2 = input("Please enter your partner's name: ")

combined_name = name1.lower() + name2.lower()

true_count = 0
for char in "true":
    true_count += combined_name.count(char)

love_count = 0
for char in "love":
    love_count += combined_name.count(char)

score = int(str(true_count) + str(love_count))

print("Your love compatibility score is: " + str(score))

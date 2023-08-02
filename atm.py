def atm_program():
    #set your pin
    pin = "2022" 
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts: #maximum attempt is 3
        entered_pin = input("Enter your PIN: ")

        if entered_pin == pin:
            print("PIN accepted. Access granted.")
            # Perform further operations here
            break
        else:
            attempts += 1
            print("Incorrect PIN. Please try again.")

    if attempts == max_attempts:
        print("Maximum PIN attempts reached. Your card is blocked.")

atm_program()

for A in range (1,11):
    print("5","*",A,"=",5*A)
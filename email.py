#this code is for email validation(to chaque that the emil is in right or wrong format)                                
email = input("Enter your email: ")
R, A, M = 0, 0, 0

if len(email) >= 6:
    if email[0].isalpha():
        if "@" in email and email.count("@") == 1:
            if email.endswith(".com") or email.endswith(".org"):
                for i in email:
                    if i.isalpha():
                        if i == i.upper():
                            A = 1
                    elif i.isdigit():
                        continue
                    elif i in ["_", ".", "@"]:
                        continue
                    else:
                        M = 1
                if R == 1 or A == 1 or M == 1:
                    print("Wrong email format")
                else:
                    print("Valid email address")
            else:
                print("Wrong email format")
        else:
            print("Wrong email format")
    else:
        print("Wrong email format")
else:
    print("Wrong email format")

def check_complexity(password):
    if len(password) >= 8:
        if any(i.isupper() for i in password):
            if any(i.islower() for i in password):
                if any(i.isdigit() for i in password):
                    if any(not i.isalnum() for i in password):
                        print("Password is strong")
                    else:
                        print("Password should contain atleast 1 special character")
                else:
                    print("Password should contain atleast 1 Number")
            else:
                print("Password should contain atleast 1 small letter")
        else:
            print("Password should contain atleast 1 capital letter")

    else:
        print("Password Should be 8 characters long") 
    

password = input("Enter a Password: ")
check_complexity(password)

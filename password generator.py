import random
import string


letters = string.ascii_letters
numbers = string.digits
special = string.punctuation

has_number = False
has_special = False
has_letter = False

while True:
    pass_length = input("\nHow many characters do you want your password? ")
    if pass_length.isdigit():
        pass_length = int(pass_length)
        
        if pass_length < 7:
            print("You can't have less than 7 characters")
            continue
        break

    else:
        print("Invalid answer")
        continue

while True:
    want_number = input("\nDo you want numbers in your password? (y/n) ").lower()
    if want_number not in ["y","n"]:
        print("invalid answer")
        continue
    break
        
while True:
    want_special = input("\nDo you want special characters in your password? (y/n)").lower()
    if want_special not in ["y","n"]:
        print("invalid answer")
        continue
    break        


password = ""
how_many_special = 0

while len(password) < pass_length:

    if want_number == "y":
        
        if want_special == "y":
                available_char = letters + numbers + special
                new_char = random.choice(available_char)  
                password += new_char
                continue
                                        
                    
        if want_special == "n":
                available_char = letters + numbers
                new_char = random.choice(available_char)  
                password += new_char
                continue




    if want_number == "n":

        if want_special == "y":
            available_char = letters + special
            new_char = random.choice(available_char)  
            password += new_char
            continue
                               
        if want_special == "n":
                available_char = letters
                new_char = random.choice(available_char)  
                password += new_char
                continue


print ("Your password is", password)
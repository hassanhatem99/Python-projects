import random

print("\n\nWelcome to our number guessing game!\n\n")
print("You will enter a positive number and try to guess one from the list of numbers from 1 to the number you entered\n\n")
difficulty= input("First, type 1 for easy and 2 for hard: ")
if difficulty == "2":
    print("Okay! Lets play...\n\n")
    #TOP OF RANGE
    top_of_range = input("Type a number: ")
    guess = 1
        
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)   
        if top_of_range <= 0:
            print("Please type a positive number next time")
            quit()
        
    else:
        print("Please type a number next time") 
        quit()  

    #USER GUESS

    random_number =random.randint(1, top_of_range)
    while True:   
    
        user_guess = input("Make a guess: ")
    
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print("Please type a number next time")
            continue    

        if user_guess <= 0:
            print("Please type a positive number next time")
            continue
        
        
        if random_number != user_guess:
            print("You got it wrong:(")
            guess = guess + 1
            continue
            
        else:
            print("You got it right!")
            print("You got it in", guess, "guesses")
            break


elif difficulty == "1":
    
    print("\nOkay! Lets play...\n\n")

    #TOP OF RANGE
    top_of_range = input("Type a number: ")
    guess = 1
        
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)   
        if top_of_range <= 0:
            print("Please type a positive number next time")
            quit()
        
    else:
        print("Please type a number next time") 
        quit()  

    #USER GUESS

    random_number =random.randint(1, top_of_range)
    while True:   
    
        user_guess = input("Make a guess: ")
    
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print("Please type a number next time")
            continue    

        if user_guess <= 0:
            print("Please type a positive number next time")
            continue
        
        
        if random_number < user_guess:
            print("You are above the number")
            guess = guess + 1
            continue

        if random_number > user_guess:
            print("You are below the number")
            guess = guess + 1
            continue


        else:
            print("You got it right!")
            print("You got it in", guess, "guesses")
            break

else:
    print("Error: Please enter 1 or 2")
    quit()

import random


options = ["rock", "paper", "scissors"]


user_wins = 0
computer_wins = 0
best_of = 0

while True:

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
   
    if best_of == 5:
        break
   
    user_pick = input("\n\nType rock/paper/scissors or Q to quit: ").lower()
    if user_pick == "q":
        break

    if user_pick not in options:
        continue

    if user_pick == computer_pick:
        print ("\nComputer picked", computer_pick)
        print("Draw!")
        continue

    best_of += 1

    print ("\nComputer picked", computer_pick)
   

    if user_pick == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins +=1

    elif user_pick == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins +=1    

    elif user_pick == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins +=1 

    else:
        print("Computer won!")
        computer_wins += 1
                          
print("\n\nYou won", user_wins, "times.")
print("Computer wins", computer_wins, "times.")
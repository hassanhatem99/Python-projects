

name= input("Hello, what's your name? \n")
print ("Hello,", name,"\nWelcome to our quiz! \nWe will ask you 5 simple questions to see how well educated you are :).")
print("Are you ready? y/n ")
ready = input()
if ready != ("y"):
    quit()
else:
    print("\nAwesome! Lets start...\n")
    score = 0

    #FIRST QUESTION
    Q1= input("Question 1: What does GUI stand for? \n")
    if  Q1.lower() == "graphical user interface":
        print ("\nCorrect!\n")  
        score = score + 1
    else:
        print("\nIncorrect :(\n")    
    
    #SECOND QUESTION
    Q2= input("Question 2: What does CPU stand for? \n")
    if  Q2.lower() == "central processing unit":
        print ("\nCorrect!\n")  
        score = score + 1
    else:
        print("\nIncorrect :(\n")

    #THIRD QUESTION
    Q3= input("Question 3: What does RAM stand for? \n")
    if  Q3.lower() == "random access memory":
        print ("\nCorrect!\n")  
        score = score + 1
    else:
        print("\nIncorrect :(\n")    
    
    #FOURTH QUESTION
    Q4= input("Question 4: What does IDE stand for? \n")
    if  Q4.lower() == "integrated development environment":
        print ("\nCorrect!\n")  
        score = score + 1
    else:
        print("\nIncorrect :(\n")

    #FIFTH QUESTION
    Q5= input("Question 5: What does HTML stand for? \n")
    if  Q4.lower() == "hypertext markup language" or "hyper text markup language":
        print ("\nCorrect!\n")  
        score = score + 1
    else:
        print("\nIncorrect :(\n")

print("You got ", str(score), "questions right out of 5\n")
print("Your score is", (score/5)*100, "%")

print("Thank you for taking our quiz:)")
        

        
    






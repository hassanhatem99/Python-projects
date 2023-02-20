months = [*range(1,13,1)]
days = [*range(1,32,1)]

while True:
    #read current date
    current_year = input("\n\nEnter current year: \n")
    if current_year.isdigit():
        current_year = int(current_year)
    else:
        print("Please enter a number next time")
        continue
    
    
    current_month = input("\nEnter current month from 1-12: \n")
    if current_month.isdigit():
        if int(current_month) not in months:
            print("Please enter a valid month")
            continue
        else:
            current_month = int(current_month)

    else:
        print("Please enter a number next time")   
        continue 

        

    

    #read birth month and day
    birth_month = input("\nEnter your birth month from 1-12: \n")
    if birth_month.isdigit():
        if int(birth_month) not in months:
            print("Please enter a valid month")
            continue
        else:
            birth_month = int(birth_month)
    else:
        print("Please enter a number next time")
        continue


    age = input("\nEnter your age: \n")
    if age.isdigit():
        age = int(age)
    else:
        print("Please enter a number next time")
        continue

    birth_year = current_year - age          

    if current_month > birth_month:
        print("\n\nYou were born in", birth_year)
        break
    elif current_month < birth_month:
        print("\n\nYou were born in", birth_year - 1) 
        break
    else:
        current_day = input("\nWhat day of the month is today? \n")
        if current_month in [4,6,9,11]:
            days = [*range(1,31,1)]
        elif current_month == 2:
            days = [*range(1,29,1)]


    if current_day.isdigit():
        if int(current_day) not in days:
            print("This month has only", days[-1], "days")
            continue
        else:
            current_day = int(current_day)

    else:
        print("Please enter a number next time")   
        continue 



    birth_day = input("\nOn what day of the month were you born? \n")
    if current_month in [4,6,9,11]:
            days = [*range(1,31,1)]
    elif current_month == 2:
            days = [*range(1,29,1)]

    if birth_day.isdigit():
        if int(birth_day) not in days:
            print("This month has only", days[-1], "days")
            continue
        else:
            birth_day = int(birth_day)

        if current_day >= birth_day:
            print("You were born in", birth_year)
            break
        elif current_day < birth_day:
            print("You were born in", birth_year - 1) 
            break    




    else:
        print("Please enter a number next time")
        continue



    
        




    
        
    
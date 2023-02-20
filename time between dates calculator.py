months = [*range(1,13,1)]
days = [*range(1,32,1)]

 #FIRST DATE
while True:
   
    print("\nFirst date:")
    
    

    month1 = input("Month: ")

    while month1[0]== "0":
       month1 = month1.replace("0", "", 1)
    if month1.isdigit():
        month1= int(month1)
        if month1 not in months:
            print("invalid month")
            continue
        
    else:
        print("Invalid month")
        continue
   
    
    
    day1 = input("Day: ")
    
    while day1[0]== "0":
       day1 = day1.replace("0", "", 1)
    if day1.isdigit():
        day1= int(day1)
        if month1 in [4,6,9,11]: 
            days = [*range(1,31,1)]

        elif month1 == 2:
            if day1 <= 29:
                year1 = input("Year: ")
            

                if year1.isdigit():
                    year1 = int(year1)

                if year1 % 4 == 0:
                    if year1 % 100 ==0 and year1 % 400 != 0:
                        days = [*range(1,29,1)]
                    else:
                        days = [*range(1,30,1)]
                else:
                    days = [*range(1,29,1)] 
                
                if day1 not in days:
                    print("This month has only", days[-1], "days")
                    continue    
                break             
            
            else:
                print("This month can have only 28 or 29 days") 
                continue               

        else:
            days = [*range(1,32,1)]

        if day1 not in days:
            print("This month has only", days[-1], "days")
            continue
    else:
        print("Invalid day")
        continue
        
    

    year1 = input("Year: ")

    while year1[0]== "0":
       year1 = year1.replace("0", "", 1)


    if year1.isdigit():
        year1 = int(year1)
    else:
        print("Invalid year")
        continue
    break
   




 
#SECOND DATE        
while True:
    
    print("\nSecond date:")
    
    

    month2 = input("Month: ")

    while month2[0]== "0":
       month2 = month2.replace("0", "", 1)
    if month2.isdigit():
        month2= int(month2)
        if month2 not in months:
            print("invalid month")
            continue
        
    else:
        print("Invalid month")
        continue
   
    
    
    day2 = input("Day: ")
    
    while day2[0]== "0":
       day2 = day2.replace("0", "", 1)
    if day2.isdigit():
        day2= int(day2)
        if month2 in [4,6,9,11]: 
            days = [*range(1,31,1)] 

        elif month2 == 2:
            if day2 <= 29:
                year2 = input("Year: ")
            

                if year2.isdigit():
                    year2 = int(year2)

                if year2 % 4 == 0:
                    if year2 % 100 ==0 and year2 % 400 != 0:
                        days = [*range(1,29,1)]
                    else:
                        days = [*range(1,30,1)]
                else:
                    days = [*range(1,29,1)] 
                
                if day2 not in days:
                    print("This month has only", days[-1], "days")
                    continue    
                break    
            else:
                print("This month can have only 28 or 29 days")
                continue

        else:
            days = [*range(1,32,1)]

        if day2 not in days:
            print("This month has only", days[-1], "days")
            continue
    else:
        print("Invalid day")
        continue
        
    

    year2 = input("Year: ")

    while year2[0]== "0":
       year2 = year2.replace("0", "", 1)

    

    if year2.isdigit():
        year2 = int(year2)
    else:
        print("Invalid year")
        continue
    break
   


year_diff = year2 - year1





#CALCULATE
if year2 >= year1:
    
    

    if month2 > month1:
        year_diff = year2 - year1
        
        if day2 >= day1:
            day_diff = day2 - day1
            month_diff = month2 - month1

        if day1 > day2:
            month_diff = month2 - month1
            month_diff-=1

            
            
            if month1 in [5,7,10,12]:
                day_diff = 30 - (day1 - day2)
                
            
            if month1 in [2,4,6,8,9,11,1]:
                day_diff = 31 - (day1 - day2)

            if month1 == 3:
                
                if year1 % 4 == 0:
                    if year1 % 100 ==0 and year1 % 400 != 0:
                        day_diff = 28 - (day1 - day2)
                    else:
                        day_diff = 29 - (day1 - day2)
                else:
                    day_diff = 28 - (day1 - day2)
                                       

    if month1 > month2:
        year_diff -=1
        month_diff = 12 - (month1 - month2)

        if day2 >= day1:    
            day_diff = day2 - day1
            month_diff = 12 - (month1 - month2)
            


        if day1 > day2:    
            month_diff = 12 - (month1 - month2)
            month_diff-=1

            
            
            if month2 in [5,7,10,12]:
                day_diff = 30 - (day1 - day2)
            
            if month2 in [2,4,6,8,9,11,1]:
                day_diff = 31 - (day1 - day2)

            if month2 == 3:
                
                if year1 % 4 == 0:
                    if year1 % 100 ==0 and year1 % 400 != 0:
                        day_diff = 28 - (day1 - day2)
                    else:
                        day_diff = 29 - (day1 - day2)
                else:
                    day_diff = 28 - (day1 - day2)

    
    if month1 == month2:
        

        if day2 >= day1:
            month_diff = 0
            year_diff = year2 - year1
            day_diff = day2 - day1


        if day1 > day2:
            year_diff -=1
            month_diff = 11
            
            if day1 > day2:
            
                if month1 in [5,7,10,12]:
                    day_diff = 30 - (day1 - day2)
                    
                
                if month1 in [2,4,6,8,9,11,1]:
                    day_diff = 31 - (day1 - day2)

                if month1 == 3:
                    
                    if year1 % 4 == 0:
                        if year1 % 100 ==0 and year1 % 400 != 0:
                            day_diff = 28 - (day1 - day2)
                        else:
                            day_diff = 29 - (day1 - day2)
                    else:
                        day_diff = 28 - (day1 - day2)
            


        if day1 == day2:
            year_diff = year2 - year1
            day_diff = 0    





if year_diff<0:
    print("Second date should be later than first date")
    quit()
if year_diff==0:
    if month1>month2:
        print("Second date should be later than first date")
        quit()
    if month_diff==0:
        if day1>day2:
                print("Second date should be later than first date")
                quit()















    
print(month_diff, "months", day_diff,"days", year_diff,"years")
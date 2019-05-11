Total_Marks=425
field = input("Please enter your field \n Biology or Computer Science? : ")
if field=="Biology" :
     English = int (input("Enter your marks for English : "))
     Biology = int (input("Enter your marks for Biology : "))
     Pakistan_Studies = int (input("Enter your marks for Pakistan_Studies : "))
     Chemistry = int (input("Enter your marks for Chemistry : "))
     Sindhi = int (input("Enter your marks for Sindhi : "))
     marks_obtained=(English+Biology+Pakistan_Studies+Chemistry+Sindhi)
     percentage=((marks_obtained/Total_Marks)*100)
     print("Your total marks are : "+str(marks_obtained))
     print("Your percentage is : "+str(percentage))
     if percentage >=80 :
         print("You achieved A+ Grade")
     elif (percentage<80 and percentage>=70) :
           print("You achieved A Grade")
     elif (percentage<70 and percentage>=60) :
           print("You achieved B Grade")
     elif (percentage<60 and percentage>=50) :
           print("You achieved C Grade")
     elif (percentage<50 and percentage>=40) :
           print("You achieved D Grade")      
     else :
           print("You are fail!!!")   



elif field=="Computer Science" :

     English = int (input("Enter your marks for English : "))
     Computer_Science = int (input("Enter your marks for Computer_Science : "))
     Pakistan_Studies = int (input("Enter your marks for Pakistan_Studies : "))
     Chemistry = int (input("Enter your marks for Chemistry : "))
     Sindhi = int (input("Enter your marks for Sindhi : "))
     marks_obtained=(English+Computer_Science+Pakistan_Studies+Chemistry+Sindhi)
     percentage=((marks_obtained/Total_Marks)*100)
     print("Your total marks are : "+str(marks_obtained))
     print("Your percentage is : "+str(percentage))
     if percentage >=80 :
         print("You achieved A+ Grade")
     elif (percentage<80 and percentage>=70) :
           print("You achieved A Grade")
     elif (percentage<70 and percentage>=60) :
           print("You achieved B Grade")
     elif (percentage<60 and percentage>=50) :
           print("You achieved C Grade")
     elif (percentage<50 and percentage>=40) :
           print("You achieved D Grade")      
     else :
           print("You are fail!!!")   
else :
   print("Invalid Field")
number = 1
while True:
    try:
        marks = int(input("Enter the Marks for the Student No %d - " %(number)))
        if marks>100 or marks<0 : print("Invalid Marks")
        else:
            if marks>=90: print("Student Number %d gets A+ " %(number)) 
            elif marks>=80 and marks<90: print("Student Number %d gets A" %(number))
            elif marks>=70 and marks<80: print("Student Number %d gets B" %(number))
            elif marks>=60 and marks<70: print("Student Number %d gets C" %(number))
            elif marks<60: print("Student Number %d gets F" %(number))
    except ValueError: print("Invalid")    
    option=input("Do you want to continue ? [Yes] or [No] ) :").strip().lower()
    if option !="yes": 
        break    
    number=number+1
print("Bye for now!!")
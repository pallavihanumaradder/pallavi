eng_marks=int(input("enter ur english marks"))
sci_marks=int(input("enter ur science marks"))
 #if condition
if eng_marks>25 and sci_marks>30: #test the condition
    print("ur elegible")
else:
    print("not elegible")
signal="red"

if signal=="red":
    print("stop")
elif signal=="yellow":
    print("get ready")
else:
    print("go")
    # nested if else statements
gender=input("enter your gender :")
age=int(input("enter ur age:"))
        
if gender=="female":
    print("Ticket is free")
else:
    if age<6:
        print("child discount")
    elif age>60:
        print("Senior discount")
    else:
        print("pay the full fare")
        
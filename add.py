h=int(input("Enter the number of days held :"))
a=int(input("Enter the number of days attend :"))
percentage= a/h*100
if(percentage<75):
    m=input("Did you hava medical issue (y/n): ")
    if(m=='y'):
        print("You are eligible - ",percentage)
    elif(m=='n'):
        print("You are not eligible - ",percentage)
    else:
        print("Enter  the valid answer :/ ")
elif(percentage>=75 and percentage<100):
    print("Your are eligible - ",percentage)
else:
    print("Invalid input, plz check it :/")

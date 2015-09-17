#Graduation Program
#Determines graduation eligibility of students.
#Created in Python 2.7.8
#By Dakota Mitchem

#Accepts user input into variables
GPA = float(input("Enter your GPA. "))
credit = input("Enter your number of credits. ")
stem = input("Enter number of math and science credits. ")
english = input("Enter number of english credits. ")
social = input("Enter number of social studies credits. ")
#Create variable for special requirements
courses = 0
#Test whether special requirements are met
if (stem >= 6 and english >= 8) or (stem >= 6 and social >= 4) or (english >= 8 and social >= 4):
    courses = 1
#Display low GPA warning
if GPA < 2.0:
    print "Academic Probation Warning!"
#Test and display for successful graduation
if credit >= 40 and GPA >= 2.0 and courses == 1:
    print "Congratulations! You can graduate!"
#Test and display for needing another semester
elif courses == 1 and (GPA < 2.0 or credit < 40):
    print "Take another semester!"
    if credit < 40 and GPA < 2.0:
        print "You can do this! Try harder next semester!"
    elif GPA < 2.0:
        print"Get your GPA up to graduate!"
    elif credit < 40:
        print"Take more major credits to graduate!"
#Test and display for special requirements not met
elif GPA >= 2.0 and credit >= 40 and (stem >= 6 or english >= 8 or social >= 4):
    print "Take more general education credits!"
#Display if no criteria is met
else:
    print "Not eligible for graduation."

"""Gradebook- accepts student grades and displays them and the grade average
   By Dakota Mitchem"""

# Accepts number of students into variable
students = input("How many Students are in your class?")
# Creates variables
sum1 = 0
gradelist = []
# Loops to accept grades into list and add them to calculate average
for x in range(0, students):
    grade = float(input("Enter a grade"))
    sum1 += grade
    gradelist.append(grade)
# Calculates average
average = sum1 / students
# Prints list and average
print "The grades are", gradelist
print "The average is", average, "%"

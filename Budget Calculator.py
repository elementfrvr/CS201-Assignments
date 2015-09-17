'''If program -Calculates and assesses budget
    By Dakota Mitchem'''
budget = 50.0 #Set budget to 50
number = input("How many oranges would you like?")  #Ask how many oranges
if number > 6:
    budget = (budget-((number*.50)*.85))  #Calculate cost for less than 6
else:
    budget = (budget-(number*.50))  #Calculate cost for more than 6
print budget  #Display budget
print"Now it's time to figure out breakfast"
choice = raw_input("Oatmeal or Microwave Meal?")  #Accept Input
if choice == "Oatmeal" or "oatmeal":  #Check if oatmeal and subtract price
    budget -= 2.5
else:  #Check if not oatmeal and subtract price
    budget -= 5
print budget  #Display remaining budget
print "Now we'll figure out dinner"
opt1 = raw_input("Meat or Vegetarian?")  #Ask if meat or vegetarian
if opt1 == "Meat":
    opt2 = raw_input("Chicken or Beef?") #Ask if chicken or beef
    if opt2 == "Chicken":
        pound = 3.00  #Set price to 3.00
    if opt2 == "Beef":
        pound = 5.00  #Set price to 5.00
if opt1 == "Vegetarian":
    opt2 = raw_input("Tofu or Nuts?")  #Ask if tofu or nuts
    if opt2 == "Tofu":
        pound = 4.50  #Set price to 4.50
    if opt2 == "Nuts":
        pound = 7.00  #Set price to 7.00
number = input("How many pounds would you like?")  #Ask if how many pounds
budget -= (pound * number)  #Subtract price
print "Remaining budget is ", budget  #Display remaining budget
if budget > 40.0:  #Display message for too little food
    print "Hmm ... You might want to buy more food.."
elif 20.0 < budget < 40.0:  #Display message for good amount of food
    print "Good job! Have a great meal and enjoy the leftovers!"
elif 0 < budget < 20:  #Display message for too much food
    print "You might have overspent a little... make it last!"
else:  #Display message for over budget
    print "You overspent, put some items back on the shelf!"

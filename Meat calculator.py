'''If Program 3-Calculates budget after buying meat
    By Dakota Mitchem'''
budget=50.00 #Set budget to 50
opt1=raw_input("Meat or Vegetarian") #Ask if meat or vegetarian
if opt1 == "Meat":
    opt2=raw_input("Chicken or Beef?") #Ask if chicken or beef
    if opt2 == "Chicken":
        pound=3.00 #Set price to 3.00
    if opt2 == "Beef":
        pound=5.00 #Set price to 5.00
if opt1 == 'Vegetarian':
    opt2=raw_input("Tofu or Nuts?") #Ask if tofu or nuts
    if opt2 == "Tofu":
        pound=4.50 #Set price to 4.50
    if opt2 == "Nuts":
        pound=7.00 #Set price to 7.00
number=input("How many pounds would you like?") #Ask if how many pounds
budget=budget-(pound*number) #Subtract price
print budget #Display remaining budget

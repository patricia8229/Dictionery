#arithmetic operators
#+ addition
#- substraction
#* multiplication
#/division
print(2**3)
#** exponential
#% modulo operator
print (10%3)
#%operator returns the remainder of a division
print (10/3)
print(48%2)
#use modulo operator to check if a year is a leap year
#// floor division
print(49//3)


#Assighnment operators
#= assigns to an identifier

add = 2+2
add +=10
print(add)
#increament operator
#decreament operator decreases by that amount
#add -=1

#comparison operators
#>greater than
#>=greater than or equal to
#<less than
#<= less than or equal to
#==equal to
#!=not equal to
#all comparison operations produces boolean


#logical operators
#when you have more than one condition
print (290>=300)
290>=300 and 70 >=60
#and - all conditions need to evaluate to true

#False and True = False
#False and False = False
#True and True = True

def lower(ls):
    return ls.lower()

e = ("Ali","Kim","Max")
res =map(lower,e)
print(list(res))

#or
#True or True = True
#True or False = True
# False or False = False

#not negates

#  today we are gonna learn about integers , floating (real) point numbers , boolean , complex numbers and operations based on them 

# INTEGERS 
print("INTEGERS \n")
var =   19
var2 = 4
total = var + var2
print(f"sum of the variables is {total}")

diffrence = var - var2
print(f"Diffrence of the variables is {diffrence}")

floating_point_division = var/ var2
print(f"Floating Point Division of the variables is {floating_point_division}")

floor_division = var // var2
print(f"Floor Division of the variables is {floor_division}")

Modulus_Operator = var %  var2
print(f"Modulus of the variables is {Modulus_Operator}")

Exponent_Operator = var **  var2
print(f"Exponent of the variables is {Exponent_Operator}")

big_value = 1_000_0000_000  #  uses underscore to imporves the readablity of the code 
print(f"The efficient way to write the big numbers is {big_value} ")

#  BOOLEAN 
print("\nBOOLEAN\n")
answer1 = True # Represents as 1
answer2 = False # Represents as 0

upcasting = var +answer1
print(f"The upcasting value of the variables is {upcasting}")

#  using boolean  typecasting 
zero =0
one =1
print(f"The typecasted value  one of  is {bool(one) }")
print(f"The typecasted value zero of  is {bool(zero)}")
# only o and none  is typecasted into false rest is typecasted as true by default

# REAL NUMBERS OR FLOATING POINT NUMBERS 

print(f"\n FLOATING POINT NUMBER \n ")
float1= 98.5
float2 = 98.499999999999

print(f"The value of float1 is {float1}")
print(f"The value of float2 is {float2}")

print(f"The diffrence bw floating value is {float1 - float2}")

import sys 
print(f"The floating point information is : {sys.float_info}")


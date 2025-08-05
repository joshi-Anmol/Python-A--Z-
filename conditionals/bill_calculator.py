order = input("Do let us know the size of your drink : \nsmall \nmedium \nlarge\n").lower()
bill = 0
if order == "small" :
    bill += 15 
    print(f"Your bill is {bill}")
elif order == "medium" :
    bill +=20
    print(f"Your bill is {bill}")
elif order == "large" :
    bill+= 25 
    print(f"Your bill is {bill}")
else :
         print("Unknown Cup Sizes")
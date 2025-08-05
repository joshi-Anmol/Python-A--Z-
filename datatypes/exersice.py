my_cart = ["apples", "bananas","milk"]
print(my_cart)

my_cart.append("bread")
print(my_cart)

my_cart.insert(0 , "ketchup")
print(my_cart)

my_cart.remove("bananas")
print(my_cart)

removed_item =my_cart.pop()
print(removed_item)

my_cart.extend(["rice" ,"butter"])
print(my_cart)

grocery_list =my_cart.sort()
print(grocery_list)

my_cart.reverse()
print(my_cart)

another_list =[ "juuice" ,"jam"]
resulting_list= my_cart + another_list
print(resulting_list)

double_grocery = my_cart*2
print(double_grocery)

string_items = "tomato cucumber spinach"
converted_list =string_items.split()
print(converted_list)
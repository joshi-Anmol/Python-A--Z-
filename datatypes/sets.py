print("ALL ABOUT SETS IN PYTHON ")

set1 ={1, 2, 3, 4, 5 }
another_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

"""  sets are immutable , unordered and uniques in nature """
print("Methods  in sets ")

set1.add(6)  # Adds an element to the set
set1.remove(5)
set1.discard(4)  # Removes an element, does not raise an error if not found
set1.pop ()
set1.update(another_set)  # Adds elements from another set
set1.clear()  # Removes all elements from the set

print("operations in sets ")
print(f"The union of set1 and another set is : {set1 | another_set}")
print(f"The union of set1 and another set is : {set1.union(another_set)}")
print(f"The intersection of set1 and another set is : {set1 & another_set}")
print(f"The intersection of set1 and another set is : {set1.intersection(another_set)}")

print(f"The diffrence of another set and set1 is : {another_set- set}")
print(f"The diffrence of another set and set1 is : {another_set.difference(set1)}")

print(f"The symmetric difference of set1 and another set is : {set1 ^ another_set}")
print(f"The symmetric difference of set1 and another set is : {set1.symmetric_difference(another_set)}")
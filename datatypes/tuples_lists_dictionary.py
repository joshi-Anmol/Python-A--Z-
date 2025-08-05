# TUPLES
""" immutable"""
tup = ("value1","value2","value3")
( key1 , key2 , key3 ) = tup
print(f"The value of tup is {key1} , {key2} , {key3}")


# LIST aka arrays 
"""mutable"""
lists= [1,2,3,4,5]
"""can work on list with many of its methods"""
# list basics methods 
lists.append(7)
print(f"The new list is : {lists}")

lists.remove(7)
print(f"The remove list is : {lists}")

lists.insert(5 ,55)
print(f"The insert list is : {lists}")
lists.pop()
print(f"Thepop list is : {lists}")

lists.reverse()
print(f"The reverse list is : {lists}")

lists.sort()
print(f"the sorted list is : {lists}")

name =["CINDRELLA"]

print(name)
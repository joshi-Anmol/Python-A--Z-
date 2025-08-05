""" Dictionary  are the set of key value pairs that are mutable and ordered set of data pairs """

from traceback import print_tb


dic ={ "key1" : "value1",
    "key2" : "value2",
    "key3" : "value3",   
    }

# The other way to create a Dictionary is 

dic_n =dict(key1="value1" , key2= "value2", key3 = "value3")  

print(f"The dictionary is : {dic}")
print(f"The other dictionary is : {dic_n}")

# Adding new data to the Dictionary 

dic["key4"] = "value4"
dic_n["key4"] = "value4"

print(f"The dictionary is : {dic}")
print(f"The other dictionary is : {dic_n}")

#  Accesing the value by their key elements 

print(f"Value element accessed by key elements : {dic["key1"]}")
print(f"Value element accessed by key elements : {dic_n["key1"]}")

# Using the "del" keyword to delete the key value pair from the dictionary 

print(f"The dictionary before using the del keyword : {dic}")
del dic["key4"]
print(f"The dictionary after using the del keyword : {dic}")

print(f"The dictionary before using the del keyword : {dic_n}")
del dic_n["key4"]
print(f"The dictionary after using the del keyword : {dic_n}")

#  Membership test 

print("key2" in dic)

#Getting all the keys in the dictionary 

print(f"All keys in the dictionary : {dic.keys()} ")
print(f"All keys in the dictionary : {dic_n.keys()} ")

# Getting all the values in the dictionary 
print(f"All values in the dictionary : {dic.values()} ")
print(f"All values in the dictionary : {dic_n.values()} ")

#  Getting all the values in the dictionary 
print(f"All items in the dictionary : {dic.items()} ")
print(f"All items in the dictionary : {dic_n.items()} ")

#  Removing the last item aka pop 
dic.popitem()
dic_n.popitem()

print(f"The dictionary after poping the last item set : {dic}")
print(f"The dictionary after poping the last item set : {dic_n}")

#  updating the whole dic with dic_n items
dic.update(dic_n)
print(f"The updated dic items are : {dic}")

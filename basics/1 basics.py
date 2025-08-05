# mutable values 
print("Mutable Objects\n")
value = 12 
print(f"intial value : {value}")
print(f"ID of intial value is {id(value)}")

value = 123
print(f"new value : {value}")
print(f"ID of  new intial value is {id(value)}\n")

# immutable values 
print("Immutable Objects\n")
value1 = set()
print(f"The inital value of value1 is {value1}")
print(f"The ID of value1 is : {id(value1)}")

value1.add("value1.1")
value1.add("value1.2")
value1.add("value1.3")

print(f"The final value of value1 is {value1}")
print(f"The ID of new value1 is : {id(value1)}")

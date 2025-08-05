customer = {
    "name": "John Doe",
    "age": 32 ,
    "city": "New York"
}
print(f"The customer dictionary is : {customer} " )

# Add "email" and "phone" to the dictionary.

customer["email"] = "johndoe@xyz.abc"
customer["phone"] = 9879879870

print(f" Is email in customer : {'email' in customer} ")

del customer["age"]

print(f"The new updated customer is {customer}")

print(customer.keys())
print(customer.values())
removed_item = customer.popitem()
print(removed_item)
print(customer.get("membership" ,"no such things"))

customer.update({"address": "221B Baker Street"})
print(customer)
#  we will learn about string basics , indexing and a bit of slicing 

"""Strings are immutable in nature"""
string1 = "Value of sting one"
string2 ="Value of string two"
print(f"The {string1} is not equal to {string2}")

# Using encoded and decoded characters 

label_text = "Spécial Label text"
print(f"This is  the label text : {label_text}")
Encoded_text = label_text.encode("utf-8")
print(f"The encoded text of label text is {Encoded_text}")
Decoded_text = Encoded_text.decode("utf-8")
print(f"The Decoded text of label text is {Decoded_text}")

# you know enough about string slicing 

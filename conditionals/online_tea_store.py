order_amount =  int(input("Enter your order cost : "))
order_price = 0 if order_amount >300 else 30
print(f"The order price of the current order is Rs. {order_price}")
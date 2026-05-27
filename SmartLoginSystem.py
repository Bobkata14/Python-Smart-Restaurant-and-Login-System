# Smart Restaurant & Login System

#Login
saved_username = input("Enter your username: ")
saved_password = input("Enter your password: ")

if saved_username == "Admin" and saved_password == "admin123":
    print("Login successful!")
else:
    print("Access denied.")
    exit()

is_logged_in = True

#Products
name1 = "Pasta Carbonara"
price1 = 3.25
quantity1 = 2

name2 = "Burger Palace"
price2 = 5.00
quantity2 = 2

name3 = "Pizza Peperoni"
price3 = 6.10
quantity3 = 3

is_delivery = True
delivery_price = 5

if is_delivery:
    grand_total = delivery_price

#Calculations
total1 = price1 * quantity1
total2 = price2 * quantity2
total3 = price3 * quantity3
subtotal = total1 + total2 + total3
grand_total = total1 + total2 + total3 + delivery_price

#Discount
if grand_total > 30:
    discount = 10
else:
    discount = 0

grand_total = subtotal + delivery_price - discount
print(" ")

#Print
print("-- Food Palace --".upper() .center(27))
print(" ")

print(f"Customer: {saved_username} \n")

print(f"{name1} x{quantity1} = {total1:.2f} €")
print(f"{name2} x{quantity2} = {total2:.2f} €")
print(f"{name3} x{quantity3} = {total3:.2f} € \n")

print(f"Subtotal: {subtotal:.2f} €")
print(f"Discount: -{discount:.2f} €")
print(f"Delivery: {delivery_price:.2f} €")
print(" ")

print("--------------------------------")
print(f"Final Total: {grand_total:.2f} € \n")

print(f"Logged in: {is_logged_in}")
print("Order Successful!")

#Overall - 5.80
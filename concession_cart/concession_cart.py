import time

#MENU
print("\n---------WELCOME TO MY CONCESSION CART--------\n")

menu = {"pop corn":"300",
        "Fries":"150",
        "Nachos":"229",
        "Samosa":"40",
        "cola":"70"}

for item in menu:
   time.sleep(0.5)
   print(f"{item:<10} : ₹{menu.get(item)}")
   
time.sleep(0.5)

print("\nplease answer these questions from menu")
time.sleep(1)
cart = []
price = 0

#Asking for snacks and its quantity
for i,item in zip(range(1,len(menu)+1),menu):
  while True:
    choice = input(f"->do you want {item}? (yes/no): ").lower()
    

    if choice == "yes":
        quantity = int(input("how many do you want?: "))
        price = int(menu.get(item))  # converts price form string to integer
        cart.append((item,price,quantity))
        break

    elif choice == "no":
      break
    
    else:          
       print("please enter either ""yes"" or ""no"" only")

# printing bill 💸

time.sleep(0.75)
print("\n\n--------------HERE IS YOUR BILL-------------\n")

cost=0
total=0

for item,price,quantity in cart:
   cost = price*quantity
   time.sleep(0.5)
   print(f"price for {item:<10} x {quantity:<2} = ₹{cost}")
   total += cost # or total = total + cost

time.sleep(1.5)
print(f"\nTOTAL AMOUNT = ₹{total}") 
time.sleep(0.70)
print("THANK YOU! VISIT AGAIN!")
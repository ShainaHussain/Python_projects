print("Welcome in Zaika Cafe")
menu = {
    "pasta":  60,
    "water": 20,
    "noodles": 70,
    "chocolate": 80,
    "fried rice": 90,
    "burger": 50,
    "pizza": 100,
    "cold-coffee": 120
    
}
print("Our Menu:")
print("---------------------")
total_order = 0
for item, price in menu.items():
    print(f"{item} :    Rs.{price}")
next_order = True
while next_order:
    order = input("Enter the name of item you want to add in your order: ").lower()
    if order in menu:
        total_order += menu[order]
        print(f"{order} added in your order")
    else:
        print(f"{order} is not available")
        another_order = input("Do you want to place another order: yes/no").lower()
        if another_order == 'yes':
            next_order = True
        else:
            next_order = False

print(f"Your total bill is : Rs. {total_order}")


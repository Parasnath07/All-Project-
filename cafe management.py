# PARAS-CAFE
menu = {
    'PIZZA':40,
    'PASTA':50,
    'BURGER':60,
    'SALAD':70,
    'COFFEE':80

}
#GREET 
print("WELCOME TO PARAS RESTAURANT")
print("PIZZA:Rs40\nPASTA:Rs50\nBURGER:Rs60\nSALAD:Rs70\nCOFFEE:Rs80\n")

order_total = 0
#80+70=150
item_1 = input("enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order ")
else:
    print("please order something else can serve you!")

another_order = input("do you want to next order?(yes\no)")
if another_order == 'yes' :
    item_2 = input("enter the name of second item = ") 
    if item_2 in menu:
        order_total +=menu[item_2] 
        print(f"item{item_2}has been added to order ")
    else:
        print(f" order item{item_2} is not available!")

print (f"the total amount of item is {order_total}")


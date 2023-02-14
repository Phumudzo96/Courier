#ask the user for the price of the package
price = float(input("Enter the price of the package: "))
#ask the user for the total distance 
km = int(input("Enter total distance of delivery in km: "))

#asking the user to select from two different options
delivery_info = input("air or freight : ")

if delivery_info == "air":
    print("You have selected air")
else:
    print("You have selected freight")

delivery_info2 = input("full insurance or limited insurance : ")

if delivery_info2 == "full insurance":
    print("you have selected full insurance")
else:
    print("You have selected limited insurance")

delivery_info3 = input("gift or no gift : ")

if delivery_info3 == "gift":
    print("You have selected gift")
else:
    print("You have selected no gift")

delivery_info4 = input("priority or standard delivery : ")

if delivery_info4 == "priority":
    print("You have selected priority")
else:
    print("You have selected standard delivery")

air = 0.35
freight = 0.25
fullInsurance = 50.00
limitedInsurance =25.00
gift = 15.00
noGift = 0.00
priority = 100.00
standarDelivery =20.00

#this when you are calulating the final cost after add the user selected from the different options
cost = km * air + price + fullInsurance + gift + priority
print(f"The full cost for this is R{cost}")
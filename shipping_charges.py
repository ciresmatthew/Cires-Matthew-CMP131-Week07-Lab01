#Matthew Cires
#CMP 131 
# Week 7
#Lab 1
#Shipping company
#10/14/26
print("----------------------------")
print("Shipping charges calculator")
print("----------------------------")
weight = float(input("Enter the weight of the package: "))
while (weight < 0 or weight > 20 ):
    weight = float(input("Error please input a correct value: "))
miles = int(input("Enter the shipping distance: "))
while (miles < 10 or miles> 3000):
    miles = int(input("Error please input valid miles: "))
if weight <= 2:
    rate = 1.10
elif 2 < weight <=6:
    rate = 2.20
elif 6 < weight <= 10:
    rate= 3.70
elif 10 < weight <=20:
    rate = 4.80
shipping_charge= rate*( miles/500)

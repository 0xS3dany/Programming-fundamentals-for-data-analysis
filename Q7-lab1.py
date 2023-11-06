import math 

x = int(input("Enter the number of glasses :" ))

y = int(input("How many glasses could be hold by each tray :"))

N = math.ceil(x/y)

print(f"The number of trays is {N} ")

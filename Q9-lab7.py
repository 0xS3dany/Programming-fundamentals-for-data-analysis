Rows = int(input("Enter the number of rows :"))

for row in range(0,Rows):
    for column in range(row+1):
        print(f"{(column+1)**2}",end="\t")
    print("\n")
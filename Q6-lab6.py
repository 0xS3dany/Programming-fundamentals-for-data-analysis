lengths = [int(x) for x in input("Enter rectangle lengths ").split()]
widths = [int(x) for x in input("Enter rectangle widths ").split()]

print("Number\tlength\twidth\tArea(approximate)")

for i in range(len(lengths)):
    print("%d\t%0.2f\t%0.2f\t%.0f"%((i+1),lengths[i],widths[i],(lengths[i]*widths[i])))
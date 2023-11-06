N = int(input("Enter a number: "))


if N < 0:
    print("The number is negative.")
else:
    
    summation = 0
    for i in range(1, N + 1):
        summation += i
    print(f"The summation of numbers from 1 to {N} is: {summation}")

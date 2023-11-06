
N = int(input("Enter the number of elements (N): "))

sum_odd = 0
sum_even = 0

for i in range(N):
    num = int(input(f"Enter number {i + 1}: "))
    
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

print(f"Sum of odd elements: {sum_odd}")
print(f"Sum of even elements: {sum_even}")

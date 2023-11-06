unit = int(input("Enter a one-digit number for the units place: "))
tens = int(input("Enter a one-digit number for the tens place: "))
hundreds = int(input("Enter a one-digit number for the hundreds place: "))

if 0 <= unit <= 9 and 0 <= tens <= 9 and 0 <= hundreds <= 9:
    three_digit_number = hundreds * 100 + tens * 10 + unit
    print(f"The 3-digit number formed is: {three_digit_number}")
else:
    print("Please enter valid one-digit numbers for the units, tens, and hundreds places.")

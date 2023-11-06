full_name = input("Enter your full name: ")

name_parts = full_name.split()

if len(name_parts) >= 2:
    first_name = name_parts[0]
    last_name = name_parts[-1]
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
else:
    print("Please enter a valid full name with both a first name and a last name.")

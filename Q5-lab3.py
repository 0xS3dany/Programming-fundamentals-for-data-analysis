grades = input("Enter a list of student grades separated by spaces: ").split()
valid_flags = []
invalid_count = 0
for grade in grades:
    grade = int(grade)
    if 0<= grade <= 100:
        valid_flags.append(1)
    else :
        valid_flags.append(0)
        invalid_count += 1 

print("a. Validity of grades:")
for i in range(len(grades)):
    print(f"Grade {grades[i]} is {valid_flags[i]}")

print(f"Number of invalid grades: {invalid_count}")

valid_grades = []
for grade in grades:
    grade = int(grade)
    if 0<= grade <101 :
        valid_grades.append(grade)

average_grade = sum(valid_grades) / len(valid_grades)
print(f"c. Average grade: {average_grade:.2f}")

highest_grade = max(valid_grades)
lowest_grade = min(valid_grades)
highest_locations = [i for i in range(len(valid_grades)) if valid_grades[i] == highest_grade]
lowest_locations = [i for i in range(len(valid_grades)) if valid_grades[i] == lowest_grade]
print(f"d. Highest grade: {highest_grade} (at positions {highest_locations})")
print(f"   Lowest grade: {lowest_grade} (at positions {lowest_locations})")

above_85 = [grade for grade in valid_grades if grade > 85]
print(f"e. Students with grades greater than 85%: {above_85} (Count: {len(above_85)})")

above_average = [grade for grade in valid_grades if grade > average_grade]

print(f"f. Students with grades greater than the average: {above_average} (Count: {len(above_average)})")

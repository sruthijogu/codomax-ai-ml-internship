num_subjects = int(input("Enter number of subjects: "))

marks = []

for i in range(num_subjects):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

total = sum(marks)
average = total / num_subjects

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\n---------- RESULT ----------")
print(f"Total Marks       : {total}")
print(f"Average Percentage: {average:.2f}%")
print(f"Grade             : {grade}")
print("----------------------------")
# Day 4 - Lists

subjects = ["Python", "AI", "Machine Learning", "Data Analytics"]

print("Subjects:", subjects)

# Accessing list elements
print("First subject:", subjects[0])

# Adding an element
subjects.append("Deep Learning")
print("After adding:", subjects)

# Removing an element
subjects.remove("AI")
print("After removing:", subjects)

# Finding the length
print("Number of subjects:", len(subjects))

# Looping through the list
print("All subjects:")

for subject in subjects:
    print(subject)
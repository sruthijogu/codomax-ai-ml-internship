# DAY 3 - LOOPS & LOOP CONTROL

# 1. For Loop
for i in range(1, 6):
    print(i)


# 2. range() with Step
for i in range(2, 11, 2):
    print(i)


# 3. Negative Step - Counting Backwards
for i in range(10, 0, -1):
    print(i)


# 4. While Loop
i = 1

while i <= 5:
    print(i)
    i = i + 1


# 5. Break
for i in range(1, 11):
    if i == 6:
        break
    print(i)


# 6. Continue
for i in range(1, 11):
    if i == 6:
        continue
    print(i)


# 7. Pass
for i in range(1, 6):
    pass


# 8. Nested Loops
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
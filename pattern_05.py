# program for Star Pattern 05

for row in range(1,6):
    for col in range(row):
        print(chr(64+row),end=' ')
    print()

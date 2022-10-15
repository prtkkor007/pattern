# program for Star Pattern 02

for row in range(6):
    for col in range(row):
        print(chr(65+col),end=' ')
    print()

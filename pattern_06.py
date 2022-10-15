# program for Star Pattern 06

space = ' '
star = '*'
for row in range(5,0,-1):
    print(space*(row),star*(6-row),end=' ')
    
    print()

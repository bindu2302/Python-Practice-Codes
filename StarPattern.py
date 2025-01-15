# Rectangle pattern
rows = 5
col = 5
for i in range(rows):
    for j in range(col):
        print('*',end=" ")
    print()

print()

# right angled traingle  - increasing pattern
for i in range(rows):
    for j in range(i+1):
        print('*',end=" ")
    print()

print() 

# decreasing pattern
for i in range(rows):
    for j in range(i,rows):
        print("*",end=" ")
    print()


print()


# Right Pascal traingle 
rows = 4
col = 5
for i in range(rows):
    for j in range(i+1):
        print('*',end=" ")
    print()
for i in range(rows):
    for j in range(i,rows-1):
        print("*",end=" ")
    print()


# butterfly Pattern
rows = 4
col = 5
for i in range(rows):
    for j in range(i+1):
        print("*",end="")
    for j in range(i,rows-1):
        print(" ",end="")
    for j in range(i,rows-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(rows):
    for j in range(i,rows-1):
        print("*",end="")
    for j in range(i+1):
        print(" ",end="")
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,rows-1):
        print("*",end="")
    print()



print()

# Diamond pattern

rows = 4
col = 5
for i in range(rows):
    for j in range(i,rows):
        print(" ",end='')
    for j in range(i):
        print("*",end='')
    for j in range(i+1):
        print("*",end='')
    print()
for i in range(1,rows):
    for j in range(i+1):
        print(" ",end='')
    for j in range(i,rows-1):
        print('*',end='')
    for j in range(i,rows):
        print('*',end='')
    print()


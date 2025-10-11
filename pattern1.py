m = int(input())

for currentRow in range(m):
    for currentCol in range(m):
        if currentCol <= currentRow:
            print(currentCol+1, end = " ")
        else:
            print(" ",end = " ")
    print("")
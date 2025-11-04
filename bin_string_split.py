givenStr = input()

countOne = 0
countZero = 0

for i in givenStr:
    if i == 0:
        countZero += 1
    elif i == 1:
        countOne += 1

if countOne % 2 == 1 or countZero % 2 == 1:
    print("-1")
else:
    currZero = 0;
    currOne = 0;
    if currZero == countZero//2 and currOne == countOne//2:


    # else:
    #     print("-1")
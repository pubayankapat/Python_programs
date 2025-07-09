def is_armstrong(num):
    power=len(str(num))
    sum=0
    for i in str(num):
        digit=int(i)
        sum +=digit**power
    return(num == sum)

lower=int(input("Enter lower limit:"))
upper=int(input("Enter upper limit:"))
print("Armstrong number between {} and {} are",lower,upper)
for i in range(lower,upper+1):
    if is_armstrong(i):
        print(i)
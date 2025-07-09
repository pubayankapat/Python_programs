#finding prime no between lower bound to upper6 bound
lower=int(input('Enter the lower bound from which you want to get prime no:'))
upper=int(input('Enter the upper bound upto which you want to get prime no:'))
print('prime numbers are:')
for num in range (lower,upper+1):
  if num>1:
    for i in range (2,num):
      if (num%i)==0:
        break
    else:
      print(num,end=' ')
#   else:
#     print(num,'is neither prime nor composite')

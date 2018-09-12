# prime or not
N = int(input('Enter the number: '))
if (N<0):
    print ('Not a valid input')
    exit()
else:
    flag=1
    for i in range (2,N):
        if(N%i==0):
            flag=0
            break
            
if (flag==1):
    print ('Number is prime')
else:
    print ('Number is not prime')
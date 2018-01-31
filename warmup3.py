#Ray Tso
#1/31/18
#warmup3.py

num=int(input('Enter a integer:'))

if num%3==0 and num%2==0:
    print(num, ' is positive and divisible by both 2 and 3')

elif num>0 and num%2==0:
    print(num, ' is divisble by only 2')
elif num>0 and num%3==0:
    print(num, ' is divisible by only 3')
else:
    print(num, ' is not divisble by 2 or 3')
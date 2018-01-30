#Ray Tso
#1/29/18
#oddEven.py

num=int(input(' Enter a number:'))


if num>0 and num%2==0:
    print(num, ' The number is positive and its even')
elif num>0 and num&2!=0:
    print(num, 'The number is positive and its odd:(')
elif num<0 and num%2==0:
      print(num, ' The number is negative and its even')
else:
    print(num, ' The number is negative and its odd')

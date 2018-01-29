#Ray Tso
#1/29/18
#fortuneTeller.py

colour=input('Pick red or blue:')
number=int(input('Pick a number from 1-4:'))


if colour=='blue' and number==1:
    print('You will be attacked by a bear')

elif colour=='blue' and number==2:
    print('You will be attacked by a alligator')

elif colour=='blue' and number==3:
    print('You will be attacked by a shark')

elif colour=='blue' and number==4:
    print('You will be attacked by a tiger')

elif colour=='red' and number==1:
    print('You will be attacked by your teacher')
    
elif colour=='red' and number==2:
    print('You will be attacked by a hippo')
    
elif colour=='red' and number==3:
    print('You will be attacked by a rhino')
    
else:
    print('You will be attacked by a lion')
    
    

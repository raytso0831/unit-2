#Ray Tso
#2/5/18
#program.py

print('You are in the woods and a bear is chasing you')
print('You come  to a river')

choice=input('Did you jump in the river:')

if choice =='yes':
    print('Thankfully you know how to swim')
    print('However you see a shark')
    choice_2=input('Did you punch the shark:')

    if choice_2 =='yes':
        print('The shark eats you and you die')
    else:
        print('The shark ignores you and you successfully cross the river')
        print('You see a another bear on the bridge and you see a car ')
        choice_3=input('Did you get in the car:')
        if choice_3 =='yes':
            print('Thankfully you know how to drive and you never see the bear again')
        else:
            print('You jump off the bridge and you die')   


else:
    print('The bear kills you')














    





































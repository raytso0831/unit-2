#Ray Tso
#1/29/18
#movie.py

age=int(input(' Enter your age:'))

if age > 17:
    print(age, 'You can watch Rated-R movies.')
    
elif age > 12:
    print(age, ' You can watch PG-13 movies.')

else:
    print(age, ' You can watch PG movies.')
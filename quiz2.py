#Ray Tso
#2/12/18
#quiz2.py

word1=input('enter a word:')
word2=input('enter a second word:')


print('Number of characters in your word:',len(word1))
print('Number of characters in your second word:',len(word2))

if len(word1)>len(word2):
    print('The first word is longer')
elif len(word1)<len(word2):
    print('The second word is longer')
else:
   print ('They are the same length')

search_of_char=input(' search for a character:')
print('Number of character in your word', word1.count(search_of_char))
print('Number of character in your second word', word2.count(search_of_char))

if 'p' in word1 and 'p' not in word2:
    print('Only the first one has the letter p')
elif 'p' not in word1 and 'p'in word2:
    print('Only the second one has the letter p')
elif 'p' not in word1 and 'p'not in word2:
    print('None of them have the letter p')
else:
    print ('both of them have the letter p')

num_1=input('enter a number:')
num_2=input('enter a number:')

if num_1+num_2==12:
    print('Correct')
elif num_1+num_2:
    print('Incorrect')





    











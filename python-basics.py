# This is a comment
# greet = 'heyyyy'
# print(len(greet))

# print(greet.upper())
# print(greet.find('y'))
# print(greet.replace('e', 'a'))


# birth_year = input('Birth year?  ')
# age = 2020 - int(birth_year)
# print(f'You  are {age-1} or {age}')


# color = input('Enter "green", "yellow", "red": ').lower()
# print(f'The user entered {color}')


# if color == 'green':
#     print('Go!')
# elif color == 'yellow':
#     print('Slow Down!')
# elif color == 'red':
#     print('Stop!')
# else:
# print('Bogus!')


# rate = int(input('Enter rate: '))
# hours = int(input('Enter hours: '))
# if hours <= 40:
#     pay = hours * rate
# elif hours > 40:
#     overtime = hours - 40
#     pay = (40*rate) + (overtime*1.5*rate)

# print(pay)


print('Pig Latin')

pyg = 'ay'
original = input('Enter a word:  ')
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print(new_word)
else:
    print('empty')

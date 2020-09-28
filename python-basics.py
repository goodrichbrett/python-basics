# --
# --
# --
#  Python Notes
# --
# --
# --


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


# print('Pig Latin')

# pyg = 'ay'
# original = input('Enter a word:  ')
# if len(original) > 0 and original.isalpha():
#     word = original.lower()
#     first = word[0]
#     new_word = word + first + pyg
#     new_word = new_word[1:len(new_word)]
#     print(new_word)
# else:
#     print('empty')


# a list is an ordered sequence of objects
# lists are mutable
# .append changes the list in place, they dont produce value - they append to list
#  .extend([]) iterates ovwe list and adds to it
# .pop() returns popped out item - give index to remove
# .remove() give value to remove
#  .clear() clears whole list
#  [::-1] reverses list into new list
# List Unpacking

# a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a)
# print(other)
# print(d)

# amazon_cart = [
#     'notebooks',
#     'lights',
#     'toys',
#     'grapes'
# ]
# print(amazon_cart[0:3])
# amazon_cart[0] = 'laptops'
# print(amazon_cart)


# Dictionary aka dict
# my_list = [
#     {
#         'a': [1, 2, 3],
#         'b': ['hello'],
#         'c': True
#     },
#     {
#         'a': [4, 5, 6],
#         'b': ['byebye'],
#         'c': False
#     }
# ]

# print(my_list[0]['a'][2])


# user = {
#     'basket': [],
#     'greet': 'sah dude'
# }
# print(user.get('age', 'wrong party bro'))


# inventory = {
#     'gold': 500,
#     'pouch': ['flint', 'twine', 'gemstone'],
#     'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
# }

# inventory.update({'pocket': ['seashell', 'strange berry', 'lint']})
# inventory.get('backpack').sort()
# inventory.get('backpack').remove('dagger')
# inventory['gold'] += 50
# print(inventory)


prices = {
    'banana': 4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3
}
stock = {
    'banana': 4,
    'apple': 3,
    'orange': 5,
    'pear': 6
}
for key, val in prices.items():
    print(f'{key} costs {val} and there are {stock[key]} in stock')
total = 0
for key in prices:
    sum = prices[key] * stock[key]
    print(f'Total cost for {key}s: ${sum}')
    total += sum

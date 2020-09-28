# print('Exercise 01: Vowel or Consonant')
# letter = input("Please enter a letter from the alphabet (a-z or A-Z):  ")
# vowels = ['a', 'e', 'i', 'o', 'u']

# if letter in vowels:
#     print(f'{letter} is a vowel')
# elif letter == 'y':
#     print(f'{letter} is sometimes a vowel ;)')
# else:
#     print(f'{letter} is a consonant')


# print('Exercise 02: Length of Phrase')
# phrase = input('Enter a word or phrase:  ')
# phrase_length = len(phrase)
# print(f'What you entered is {phrase_length} characters long')


# print('Exercise 03: Calculate Dog Years')
# age = int(input("Input a dog's age in human years: "))
# dog_years = (age * 7) + 6
# print(f"The dog's age in dog years is {dog_years}")


# print('Exercise 04: What kind of triangle?')
# length1 = int(input('First length:  '))
# length2 = int(input('Second length:  '))
# length3 = int(input('Third length:  '))
# if length1 == length2 and length1 == length3 and length2 == length3:
#     print(
#         f'A triangle with side {length1}, {length2}, and {length3} is equilateral')
# elif length1 != length2 and length1 != length3:
#     print(
#         f'A triangle with side {length1}, {length2}, and {length3} is scalene')
# elif length1 == length2 or length1 == length3 or length2 == length3:
#     print(
#         f'A triangle with side {length1}, {length2}, and {length3} is isosceles')


# print('Exercise 05: Fibonacci sequence for the first 50 terms')
# x = 0
# y = 1
# results = []
# while len(results) < 50:
#     print(y)
#     results.append(y)
#     x = y
#     y = x + y


print('Exercise 06: What is the season?')
month = input(' Enter the month of the year(Jan - Dec):  ')
day = int(input('Enter the day of the month:  '))
winter = ('Jan', 'Feb', 'Mar')
spring = ('Apr', 'May', 'Jun')
summer = ('Jul', 'Aug', 'Sep')
if month in winter:
    season = 'winter'
elif month in spring:
    season = 'spring'
elif month in summer:
    season = 'summer'
else:
    season = 'fall'

if month == 'Mar' and day > 19:
    season = 'spring'
elif month == 'Jun' and day > 20:
    season = 'summer'
elif month == 'Sep' and day > 21:
    season = 'fall'
elif month == 'Dec' and day > 20:
    sseason = 'winter'

print(f'The season is {season}')

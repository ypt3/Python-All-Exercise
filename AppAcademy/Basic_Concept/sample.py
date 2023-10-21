def average(num1, num2):
    return (num1/num2)

print(average(6,2))

print("Spaghetti".index("h"))
print("Spaghetti".index("t"))
print("Spaghetti".count("t"))
print('''We choose to go to the moon in this decade and do the other things,
not because they are easy, but because they are hard, because that goal will
serve to organize and measure the best of our energies and skills, because that
challenge is one that we are willing to accept, one we are unwilling to
postpone, and one which we intend to win, and the others, too.
'''.count('the '))

first_name = "Billy"
last_name = "Bob"
print(f'Your name is {first_name} {last_name}')

shopping_list = ['bread', 'milk', 'eggs']
print(',..'.join(shopping_list))

print('{:,}'.format(1234567890))

import datetime

d = datetime.datetime(2020, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))

width = 8
print(' decimal         hex     binary')
print('-'*27)
for num in range(1,16):
    for base in 'dxb':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print()

# a = "abcd"
# a[0] = "z"
# print(a)
# Traceback (most recent call last):
#   File "sample.py", line 39, in <module>
#     a[0] = "z"
# TypeError: 'str' object does not support item assignment

def last_three(a, b):
    return a[-3:].lower() == b.lower()

print(last_three("Power", "wer"))
print(last_three("Application", "App"))


def is_palindrome(a):
    return a[::-1] == a

print()
print(is_palindrome("kayak"))
print(is_palindrome("app"))
print(is_palindrome("valid"))
print(7j)


def is_prime(n, i=2):
    if n <= 2:
        return True if n == 2 else False
    if n % i == 0:
        return False
    if n < i*i:
        return True

    return is_prime(n, i+1)


print(is_prime(1))
print(is_prime(2))
print(is_prime(3))

i = 1
i += 5
print(i)
i **= 2
print(i)

a = 'what'

if a:
    print(f'{a} is true')
else:
    print('it is false')

def divisible_by_five(n):
    '''
    this is test
    '''
    if n < 0:
        n = abs(n)
    return n % 5 == 0


try:
    str = 'hello'
    str[0] = 'm'
    print(str)
except TypeError as e:
    print(e, "Not str type")
finally:
    print('I happen regardless of any exceptions.')

try:
    print(x)
except NameError as e:
    print(e, 'No such variable')
finally:
    print('I happen regardless of any exceptions.')

def print_list(list):
    result = []
    for i in range(len(list)):
        result.append(i)
    print(result)

lst1 = [1, 2, 5, 1429]
print_list(lst1)

count = 0
total = 0

while total < 1000000:
    if total == 0:
        total = 0.01
    else:
        total *= 2
    count += 1

print('Double', count, 'times')
print(f'${total:,}')

def is_valid_hex_code(list):
    if list[0] != '#' or len(list) != 7:
        return False
    i = 1
    while i < len(list):
        char = list[i].lower()
        if not char.isdigit():
            if char != 'a' and char != 'b' and char != 'c' and char != 'd' and char != 'e' and char != 'f':
                return False
        i += 1
    return True


print(is_valid_hex_code("#CD5C5C"))  #> True




def find_majority_char(s):
    n = len(s)
    char_count = {}

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char, count in char_count.items():
        if count > n/2:
            
            return char
    print(n//2)
    return None


text = "abbcccdddd"
print(find_majority_char(text))


def numJewelsInStones(jewels, stones):
    jewel_set = set(jewels)
    count = 0

    for stone in stones:
        if stone in jewel_set:
            count += 1
    return count

jewels = "aA"
stones = "aAAbbbb"
result = numJewelsInStones(jewels, stones)
print(result)


# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a)
# print(b)

# print(a | b)
# print(a & b)
# print(a - b)
# print(b - a)
# print(a ^ b)
# print(a + b)

# a = set('banana')
# b = set('scarab')
# print(a)
# print(b)

# print(a | b)
# print(a.union(b))
# print(a.intersection(b))
# print(a.symmetric_difference(b))
# print(a.difference(b))
# print(b.difference(a))

basket = ['apple', 'banana', 'apple', 'orange', 'pear']
print(basket)
print(set(basket))

purchasingEmails = {'bob@gmail.com', 'sam@yahoo.com', 'riley@gmail.com'}
helpEmails = {'jo@gmail.com', 'cathy@gmail.com', 'al@gmail.com'}
print('Users making a purchase and also calling help desk')
print(set(purchasingEmails) & set(helpEmails))


posts = [
    {"title": "All about list", "tags": ("fun", "informative", "lists")},
    {"title": "Tuple Trouble", "tags": ("fun", "tuple")},
    {"title": "Sparking Sets", "tags": ("informative", "numbers")},
]

allTags = []
for i in range(len(posts)):
    print(posts[i]["tags"])
    allTags.extend(posts[i]["tags"])

print(allTags)
allTags = list(set(allTags))
allTags.sort()
print(allTags)


lst = [1, 2, 3, 4, 5]
set_of_lst = set(lst)

st = set()
st.update(lst)
print(st)

def add_to_set(st, lst):
    return st | set(lst)

st = {1, 2, 3, 4}
lst = [12, 4, 42, 93, 2, 85]
print(add_to_set(st, lst))


def left_diff(set1, set2):
    return set1 - set2

set1 = {1, 2, 5, 10}
set2 = {2, 6, 10, 12}

print(left_diff(set1, set2))


def remove_repeats(str1, str2):
    str1 = set(str1)
    str2 = set(str2)
    return str1 ^ str2

str1 = 'aloha'
str2 = 'bonjour'

print(remove_repeats(str1, str2))

def check_binary(str1):
    str_set = set(str1)
    return str_set == {'0', '1'} or str_set == {'1'} or str_set == {'0'}

str1 = '1010001010010100101'
str2 = '1010010015010101010'

print(check_binary(str1))       # True
print(check_binary(str2))       # False


def findJudge(n, trust):
    trust_count = [0] * (n+1)

    for a, b in trust:
        trust_count[a] -= 1
        trust_count[b] += 1

    for i in range(1, n + 1):
        if trust_count[i] == n - 1:
            return i
    
    return -1

n = 4
trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
result = findJudge(n, trust)
print(result)


users = [
        {'id':123344, 'displayName':'Joe Smith', 'email':'joe.smith@gmail.com'},
        {'id':123222, 'displayName':'Ben Smith', 'email':'ben.smith@gmail.com'},
        {'id':333333, 'displayName':'Allen Smith', 'email':'allen.smith@gmail.com'},
    ]

# print(users)

def sorter(user):
    return user['displayName'].lower()

users.sort(key=sorter)
# print(users)

reverseUsers = sorted(users, key=sorter, reverse=True)
print(reverseUsers)

print('all cases: any items is false')
title1 = ['Mr', 'Mrs', 'Ms']
title2 = ['Mr', 'Mrs', 'Ms', '']
title3 =[]
print(all(title1))
print(all(title2))
print(all(title3))

print('any case: any item is true')
feedback1 = ['', '', '', '']
feedback2 = ['so much fun!', '', '', '']
feedback3 = []

print(any(feedback1))
print(any(feedback2))
print(any(feedback3))


scores = [90, 86, 91, 62, 99, 88, 90]
print(scores)

def isA(num):
    return num >= 90

aScore = filter(isA, scores)
print(aScore)
print(list(aScore))

def getGrade(num):
    if num >= 90:
        return 'A'
    elif num <= 90 and num >= 80:
        return 'B'
    elif num <= 80 and num >= 70:
        return 'C'
    elif num <= 70 and num >= 60:
        return 'D'
    else:
        return 'F'
    
grades = list(map(getGrade, scores))
# print(grades)

print('ZIPPED GRADED AND SCORES')
combined = list(zip(scores, grades))
print(combined)


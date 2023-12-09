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

def cat_verify(cat_list):
    same_breed = all(cat['breed'] == cat_list[0]['breed'] for cat in cat_list)

    # up_for_adoption = any(not cat['adopted'] for cat in cat_list)
    up_for_adoption = any(map(lambda cat: cat['adopted'] == False, cat_list))

    return same_breed, up_for_adoption 

cat_list = [
    {
        "name": "Lenny",
        "breed": "Ragdoll",
        "adopted": False
    },
    {
        "name": "Roger",
        "breed": "Siamese",
        "adopted": False
    },
    {
        "name": "Katya",
        "breed": "Persian",
        "adopted": True
    }
]

result = cat_verify(cat_list)
print(result)


cards = [
    {
        "company": "Wells Fargo",
        "card_name": "Active Cash",
        "annual_fee": 0,
        "intro_reward_type": "cash",
        "intro_reward_amount": 200,
        "num_users": 20
    },
    {
        "company": "Chase",
        "card_name": "Sapphire Preferred",
        "annual_fee": 95,
        "intro_reward_type": "points",
        "intro_reward_amount": 60000,
        "num_users": 54
    },
    {
        "company": "Citi",
        "card_name": "Diamond Preferred",
        "annual_fee": 0,
        "intro_reward_type": "cash",
        "intro_reward_amount": 150,
        "num_users": 13
    }
]

def sorter(card):
    return card['num_users']

def sort_cards(card_list):
    return sorted(card_list, key=sorter, reverse=True)

print(sort_cards(cards))


def sorter(teacher):
    return teacher['classroom']['capacity']

def sort_teachers_by_classroom_capacity(teachers):
    teachers = sorted(teachers, key=sorter)
    return list(map(lambda teacher: teacher['name'], teachers))


teachers = [
    {
        "name": "Emily Richardson",
        "subjects": ["Geometry", "Geometry Honors"],
        "years_active": 5,
        "classroom": {
            "building_id": "A",
            "room_number": 12,
            "capacity": 45
        }
    },
    {
        "name": "Richard Emilyson",
        "subjects": ["English 11", "AP English Language"],
        "years_active": 12,
        "classroom": {
            "building_id": "J",
            "room_number": 42,
            "capacity": 60
        }
    },
    {
        "name": "Richly Emiardson",
        "subjects": ["Chemistry", "Chemistry Honors", "AP Chemistry"],
        "years_active": 8,
        "classroom": {
            "building_id": "C",
            "room_number": 5,
            "capacity": 32
        }
    },
]

print(sort_teachers_by_classroom_capacity(teachers))



phones = [
    {
        "brand": "Apple",
        "model": "iPhone 13 Pro",
        "cost": 929,
        "color": "alpine green"
    },
    {
        "brand": "Samsung",
        "model": "Galaxy S22+",
        "cost": 999,
        "color": "black"
    },
    {
        "brand": "Google",
        "model": "Pixel 6",
        "cost": 599,
        "color": "kinda coral"
    },
    {
        "brand": "Apple",
        "model": "iPhone 13 Pro",
        "cost": 929,
        "color": "gold"
    },
    {
        "brand": "Google",
        "model": "Pixel 6",
        "cost": 599,
        "color": "stormy black"
    }
]

def get_unique_models(phone_list):
    model = []
    return filter(lambda phone: model.append(phone['model']) is None if phone['model'] not in model else False, phone_list)

def map_to_names(phone_list):
    return list(map(lambda phone: phone['model'], phone_list))

unique_models = get_unique_models(phones)
model_names = map_to_names(unique_models)

print(list(model_names))  # ['iPhone 13 Pro', 'Galaxy S22+']


# squares = map(lambda x: x**2, range(10))
# print(squares)
# print(list(squares))

squares = [i**2 for i in range(10)]
print(squares)
# print(list(squares))

lst = [1,2,'string',True,None]
new = [i for i in lst]
print(new)

keys = ['age', 'name', 'height']
values = [32, 'Corina', 1.4]

# d = {keys[i].title(): values[i] for i in range(len(keys))}
d = { key: value for key, value in zip(keys, values)}
print(d)

# teller = []
# teller.append("Great Customer")
# print(teller)
# teller.pop()
# print(teller)
# teller.append("Process deposit")
# print(teller)
# teller.append("Phone Ring")
# print(teller)
# teller.pop()
# teller.append("Greet Caller, Anser question")
# print(teller)
# teller.pop()
# print(teller)
# teller.pop()
# print(teller)


processor = []
processor.append({"type": "path", "path":"", "header":[], "cookies":[]})
processor.append({"type": "api", "function":"", "parameters":[]})
processor.append({"type": "email", "address":"ji@yahoo.com", "subject":""})
print("processor", processor)

for i in range(len(processor)):
    item = processor.pop(0)
    print("PROCESSING ITEM", item)
    print("Reaming", processor)



# class StrNumeric:
#     def __init__(self, value):
#         if not isinstance(value, str) or not value.isnumeric():
#             raise Exception("String value can have only numeric characters.")
            
#         self.val = value
#     def __add__(self, thing_2):
#         return int(self.val) + int(thing_2)


# str_1 = StrNumeric("1")
# print(str_1 + 2) # 3

# str_44 = StrNumeric("44")
# print(str_44 + 6) # 50


class LinkedListIterator:
    def __init__(self, head) -> None:
        self._current = head 

    def __iter__(self):
        return self 
    
    def __next__(self):
        if not self._current:
            raise StopIteration
        else: 
            value = self._current._value
            self._current = self._current._next
            return value

class Node: 
    def __init__(self, value) -> None:
        self._value = value 
        self._next = None 
    

class LinkedList: 
    def __init__(self) -> None:
        self._head = None 
        self._tail = None 
        self._length = 0
    
    def __iter__(self):
        return LinkedListIterator(self._head)
    

    def add(self, value):
        new_node = Node(value)

        if self._head is None: 
            self._head = new_node
        else: 
            self._tail._next = new_node
        
        self._tail = new_node
        self._length += 1
        return self 


linked_list = LinkedList()
linked_list.add('node 1')
linked_list.add('node 2')
linked_list.add('node 3')
linked_list.add('node 4')
linked_list.add('node 5')

# this loop should print "Current node: node x" five times 
# for each node in the linked list
for i in linked_list:
    print(f"Current node: {i}")
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

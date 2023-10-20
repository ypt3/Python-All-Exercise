def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)

result = factorial(4)
print(result)


def validate(num):
    if (num < 1 or num < 10):
        print("Out of range")
    elif (num != int(num)):
        print("Not an integer")
    else:
        print("You are right")
        return True
    return False

print(validate(-5))
print(validate(2.5))
# print(validate("sijjgi"))


def prime_Number(n, i=2):
    if n == i:
        return True
    elif n % i == 0:
        return False
    return prime_Number(n, i+1)

n = 972
if prime_Number(n):
    print("Yes, ",n," is prime")
else:
    print("No,",n, "is not a prime")


def prime_number2(n):
    for i in range(2, 1+n//2):
        if n % 1 == 0:
            return False
        return True

n = 979
if prime_number2(979):
    print("Yes, ", n, " is prime")
else:
    print("No,", n, "is not a prime")

nums = [2,1,2]

for i in range(len(nums) -3, -1, -1):
    if nums[i] + nums[i+1] > nums[i+2]:
        print(nums[i] + nums[i + 1] > nums[i + 2])
    else:
        print(None)


def seq_of_numbers(term):
    term += ' '
    i = 0
    current_count = 1
    res = ""
    while i < len(term)-1:
        if term[i] != term[i+1]:
            res = res + str(current_count) + term[i]
            current_count = 1
        else:
            current_count += 1
        i += 1
    return res

print(seq_of_numbers("1211"))
print(seq_of_numbers("111221"))

def cap_space(str):
    result = ""
    i = 0
    while i < len(str):
        if str[i].isupper():
            result += " "
        result += str[i]
        i += 1

    return result.lower()

print(cap_space("helloWorld"))

def char_count(a, b):
    count = 0
    i = 0
    while i < len(b):
        if a == b[i]:
            count += 1
        i += 1
    return count

print(char_count("a", "App Academy"))

def vowel_count(str):
    count = 0
    vowel = "aeiouAEIOU"
    i = 0
    while i < len(str):
        if str[i] in vowel:
            count += 1
        i += 1
    return count

print(vowel_count("App Academy"))

def add_upper(str):
    result = ""
    i = 0
    while i < len(str):
        if str[i] == str[i].upper():
            result += str[i]
        i += 1
    return result

print(add_upper("ApPlE"))

import re

def valid_zip_code(zip):
    pattern = "^\d{5}(?:[-\s]\d)"
    valid = re.search(pattern, zip)
    if valid:
        return zip
    else:
        return "The zip code you entered is invalid"
    
zip1 = '47243'
zip3 = '01237-1238'
print(valid_zip_code(zip1))


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
print(validate("sijjgi"))
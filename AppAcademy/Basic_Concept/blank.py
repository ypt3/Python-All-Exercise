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

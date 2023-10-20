def greeting(name, saying="Hello"):
    print(saying, name)

greeting(name="Catherine")

topUpper = lambda s: s.upper()

print(topUpper("test"))

xor = lambda left, right: left != right
print(xor(True, True))



def print_powers_of(base, exp=1):
    i = 1
    while i <= exp:
        print(base**i)
        i += 1

print_powers_of(15)
print_powers_of(2, 5)
print_powers_of(exp=5,base=7)

def greeting_maker(salutation):
    def greeting(name):
        return f"{salutation} {name}"
    return greeting

hello = greeting_maker("hello")
hiya  = greeting_maker("Hiya")
print(hello("Catherine"))
print(hiya("Catherine"))


def add(a, b, *args):
    total = a + b
    for i in args:
        total += i
    return total

print(add(1, 2))
print(add(1, 2, 3))


def print_names_and_countries(greeting, **kwargs):
    for k, v in kwargs.items():
        print(greeting, k, "from", v)

print_names_and_countries("Hi", 
                          Catherine="Seattle",
                          Alan="Sunnyvale",
                          Tom="Nowhere")

def example(arg1, arg2, *args, **kwargs):
    pass

def welcome():
    print("welcome")

def calc_sum(a, b):
    return a + b

welcome()
print(calc_sum(1,2), "is 3?", calc_sum(1,2) == 3)

def sample_function(input, b, c):
    print(input + b + c)

def sample_function(a, b, input):
    print(a + b + input)

# sample_function(input = "asdf", "a", "b")      # ERROR
sample_function("asdf", "a", input = "b")      # VALID

# Traceback (most recent call last):
#   File "/Users/alantsai/Desktop/PythonNEW/Python-All-Exercise/AppAcademy/Basic_Concept/blank1.py", line 70, in <module>
#     sample_function(input = "asdf")      # ERROR
#     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: sample_function() missing 2 required positional arguments: 'b' and 'c'

def string_multi_print(str):
    return lambda i: print(str * i)
string_multi_print('hello ')(2)


def two_sum(nums, target):
    num_indices = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_indices:
            return [num_indices[complement], i]
        
        num_indices[num] = i
    
    return []

nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)
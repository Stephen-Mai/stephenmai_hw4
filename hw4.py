def add_numbers(a,b):
    return a+b

add_lambda = lambda a,b: a+b

print(add_numbers(3,5))
print(add_lambda(3,5))

print("------------------")

def join_words(a,b,c):
    return a+ " " + b +c

join_lambda = lambda a,b,c: a+" "+b+c
print(join_words("Hello", "world", "!"))
print(join_lambda("Hello", "world", "!"))

print("------------------")

def countdown(n):
    if n <= 0:
        print(0)
    else:
        print(n)
        countdown(n-1)
countdown(5)

print("------------------")

def greet(name):
    return "Hello " + name + "!"
print(greet("Alice"))

print("------------------")

def repeat_phrase(phrase, times=2):
    return phrase * times

print(repeat_phrase("Hi! "))
print(repeat_phrase("Hi! ", 3))

print("------------------")

def apply_function(func, value):
    return func(value)

print(apply_function(lambda x: x.upper(), "hello"))

print("------------------")

def safe_divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error: cannot divide by zero"
    except TypeError:
        print("Error: Both arguments must be numbers")
    finally:
        print("Division attempted")


print(safe_divide(6, 2))
print(safe_divide(6, 0))

print("-------------------")

def check_age(age):
    if age < 0 or not isinstance(age, int):
        return "Age must be a positive integer"
    return True

print(check_age(6))
print(check_age(-3))

print("-------------------")

def parseInt(s):
    try:
        return int(s)
    except ValueError:
        return "Could not convert"

print(parseInt("1"))
print(parseInt("hello"))
print("-------------------")

numbers = [5,4,3,2,1]

iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

print("-------------------")

words = ["hello", "world", "my", "name", "is", "stephen"]

uppercase_words = (word.upper() for word in words)

for word in uppercase_words:
    print(word)
print("-------------------")


class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current + 1

countdown = Countdown(5)

for number in countdown:
    print(number)

print("-------------------")

import itertools

colors = ["red", "blue", "green"]

color_cycle = itertools.cycle(colors)

for x in range(6):
    print(next(color_cycle))
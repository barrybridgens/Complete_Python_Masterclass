# Functions

# arguments

def add_function(arg1, arg2):
    print(arg1 + arg2)

print(add_function(5, 6))

# return values

print('Return values ...')

def add_function2(arg1, arg2):
    ans = arg1 + arg2
    return ans

result = add_function2(5, 6)

print(result)

# passing functions as arguments

print('Passing functions as arguments')

def mult(a, b):
    m = a * b
    return m

def func(f):
    res = f(3,9)
    return res

print(func(add_function2))
print(func(mult))


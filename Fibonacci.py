num = int(input())

def fibonacci(n):
    if n == 0:
         return [0]
    elif n == 1:
        return [0, 1]
    else:
        lst = fibonacci(n-1)
        lst.append(lst[-1] + lst[-2])
        return lst
fib = (fibonacci(num)[:-1])
print(*(fib), sep='\n')

# other method
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b


# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
def fib(x):
    """Calculates the fibonacci number"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 2) + fib(x - 1)  # recursion


print('Fibonacci number is: ', fib(int(input('Enter a positive number: '))))

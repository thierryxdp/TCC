def fatorial(n):
    i = 0
    factorial = 1
    while n!=0:
        factorial = factorial*i
        i = n - 1
    return factorial
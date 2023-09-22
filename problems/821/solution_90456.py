def fatorial(n):
    i = n-1
    while i > 0:
        n *= i
        i-=1
    return n
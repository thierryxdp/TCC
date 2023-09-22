from math import sqrt

def qtd_divisores(n):
    yield 1
    for i in range(2,int(sqrt(n)) + 1):
        if n % i == 0
        yield i
        
    yield n
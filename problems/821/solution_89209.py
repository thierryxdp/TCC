def fatorial (x):
    i=x-1
    fact = x
    while i >= 1:
        fact = fact*(x-i)
        i = (x-1)-1    
    return fact
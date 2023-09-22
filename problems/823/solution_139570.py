def fatorial(n):  
    acum = 1
    x = 1
    while x <= n:
        acum *= x
        x += 1
    return acum
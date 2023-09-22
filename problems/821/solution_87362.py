def fatorial(num):
    a=list(range(num,-1,-1))
    total=1
    for elemento in a:
        total=total*elemento
    return total
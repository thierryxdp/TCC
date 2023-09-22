def fatorial(n):
    x = 0
    y = 1
    lista = range(n,0,-1)
    while x < len(lista):
        y = y*lista[x]
        x = x + 1
    return y
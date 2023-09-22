def fatorial(n):
    i = 0
    lista = list(range(n))
    res=0
    while i < lista:
        res += lista[i]*lista[i+1]
    return res
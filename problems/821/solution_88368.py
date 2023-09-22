def fatorial(n):
    lista = list(range(n+1))
    lista = lista[1:]
    i = 0
    res = 0
    while i < len(lista):
        res += lista[i] * lista
        return res
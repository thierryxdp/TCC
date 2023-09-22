def fatorial(n):
    lista = list(range(n+1))
    lista = lista[1:]
    i = 0
    res = 0
    if n == 1:
        return 1
    while i < len(lista):
        res += lista[i] * lista[i+1]
        return res
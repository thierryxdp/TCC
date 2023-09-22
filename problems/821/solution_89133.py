def fatorial(n):
    lista = []
    k = 2
    while k <= n:
        lista = lista + [k]
        k = k+1
    fat = 1
    x = 0
    while x < len(lista):
        fat = fat * lista[x]
        x = x + 1
    return fat
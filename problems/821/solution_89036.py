def fatorial(n):
    lista = [n]
    while n != 1:
        n = n - 1
        lista += [n,]
    i = 0
    lista2 = []
    while i < len(lista):
        mult = lista[i] * lista[i+1]
        lista2 += [mult,]
        i = i + 1
    return mult
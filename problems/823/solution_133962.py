def faltante(lista):
    ln = len(lista)
    l = list(range(1,lista[-1]))
    i = 0
    while l[i] == lista[i]:
        i = i + 1
    if lista[i] != l[i]:
        r = l[i]
    return r
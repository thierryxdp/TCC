def faltante(lista):
    i = 1
    n = 0
    list.sort(lista)
    while i < len(lista)+1:
        if i == lista[i]:
            n = n+1
        i = i + 1
    return n
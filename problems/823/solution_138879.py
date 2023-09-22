def faltante(lista):
    i = 0
    s = 
    n = 0
    list.sort(lista)
    while i<len(lista):
        if lista[i] != n+1:
            s += [n+1,]
        i += 1
        n += 1
    return int(s)
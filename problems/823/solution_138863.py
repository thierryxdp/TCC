def faltante(lista):
    i = 0
    s = []
    n = 0
    lista1 = list.sort(lista)
    while (i+1)<len(lista):
        if  lista1[i] == n:
            s += s + [n]
        i += i +1
        n += n + 1
        return s
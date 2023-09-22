def faltante(lista):
    i = 0
    s = []
    n = 0
    lista1 = list.sort(lista)
    while i<len(lista):
        if  lista1[i] == list(n+1):
            s += s + list(n)
        i += i +1
        n += n + 1
        return s
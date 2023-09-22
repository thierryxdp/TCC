def faltante(lista):
    i = 0
    s = []
    n = 0
    soma= (((1+len(lista))*(len(lista)))/2)
    list.sort(lista)
    while i<len(lista):
        if sum(lista) != soma:
            s += [n+1,]
        i += 1
        n += 1
    return list.index(s,i)
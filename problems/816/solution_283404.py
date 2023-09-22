def maiores(lista, n):
    list = lista
    list.append(n)
    list.sort()
    
    list = list[(list.index(n)):]
    return list
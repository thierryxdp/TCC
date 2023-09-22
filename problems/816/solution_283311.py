def maiores(lista,num):
    lista.append(num)
    lista.sort()
    del lista[:lista.index(num)]
    return lista
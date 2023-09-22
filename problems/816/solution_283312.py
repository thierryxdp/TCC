def maiores(lista,num):
    lista.append(num)
    lista.sort()
    del lista[:lista.index(num)]
    lista.remove(num)
    return lista
def maiores(lista,num):
    lista.append(num)
    lista.sort()
    lista.remove(num)
    del lista(:lista.index(num))
    return lista
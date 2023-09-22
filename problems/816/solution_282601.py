def maiores(lista,num):
    list.insert(lista,0,num)
    lista.sort()
    x = lista.index(num)
    del lista[0:x+1]
    return lista
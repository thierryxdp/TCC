def maiores(lista,num):
    list.insert(lista,0,num)
    y= lista.sort()
    x = y.index(num)
    del lista[0:x+1]
    return lista
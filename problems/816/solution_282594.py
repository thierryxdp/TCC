def maiores(lista,num):
    list.insert(lista,0,num)
    sorted(lista)
    x= list.index(lista,num)
    del lista[0:x]
    return lista
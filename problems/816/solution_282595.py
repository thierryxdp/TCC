def maiores(lista,num):
    list.insert(lista,0,num)
    y= sorted(lista)
    x= list.index(y,num)
    del lista[0:x]
    return lista
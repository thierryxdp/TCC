def maiores(lista,num):
    list.insert(lista,0,num)
    y= list.sort(lista)
    x= list.index(y,num)
    del lista[0:x+1]
    return lista
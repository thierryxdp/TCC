def maiores(lista, numero):
    list.insert(lista,0,numero)
    list.sort(lista)    
    del lista[0:lista.index(numero)+1]
    return lista
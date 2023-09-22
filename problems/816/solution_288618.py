def maiores(lista, numero):
    list.insert(0,numero)
    list.sort(lista)    
    del lista[0:lista.index(n)+1]
    return lista
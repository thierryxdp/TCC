def maiores(lista,n):
    lista.append(n)
    lista.sort()
    lista=lista[lista.index(n)+1]
    
    list.remove(lista, n)
    
    return lista
def maiores(lista,n):
    l_clone=lista[:]
   	l_clone.sort()
    b=l_clone[n-1:]
    lista=b
    return lista
def maiores(lista,n):
    lista1=list.extend(lista,n)
    lista2=lista1.sort()
    a=lista2.index(n)
    return lista2[a:]
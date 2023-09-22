def maiores(lista,n):
    lista=sorted(lista)
    if n in lista:
        lista1=lista[0:n]
        return lista1
    else:
        return lista[n:]
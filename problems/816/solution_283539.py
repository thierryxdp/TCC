maiores(lista,n):
    lista2=list.sort(lista)
    ordem=list.index(lista,n)
    if n in lista:
        return lista2[ordem:]
def maiores(lista,n):
    lista2=list.sort(lista)
    ordem=lista2.index(n)
    if n in lista:
        return lista2[ordem:]
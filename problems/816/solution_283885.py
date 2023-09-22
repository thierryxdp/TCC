def maiores(lista,n):
    lista2=list.sort(lista)
    a=int.index(lista2,n)
    if n in lista:
        return lista2[a:]
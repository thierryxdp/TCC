def maiores(lista,n):
    lista=list.sort(lista)
    if [n] in lista:
        del lista[:(list.index(lista,n))]
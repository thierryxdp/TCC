def maiores(lista_numeros,n):
    lista=lista_numeros+[n]
    list.sort(lista)
    lista=str(lista)
    str.partition(lista,n)
    return lista
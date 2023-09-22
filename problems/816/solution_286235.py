def maiores(lista_numeros,n):
    lista=lista_numeros+[n]
    list.sort(lista)
    list.remove(lista,lista[-1])
    list.remove(lista,n)
    return lista
def maiores(lista_numeros,n):
    lista=lista_numeros+[n]
    list.sort(lista)
    list.remove(lista,lista[n:])
    list.remove(lista,n)
    return lista
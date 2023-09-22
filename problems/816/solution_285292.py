def maiores(lista_numero,n):
    lista1 = lista_numero
    list.insert(lista1,-1,n)
    list.sort(lista1)
    lista_nova = lista1[list.index(lista1,n)+1:]
    return lista_nova
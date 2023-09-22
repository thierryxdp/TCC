def maiores(lista,n):
    ''''''
    lista_com_n= lista + [n]
    list.sort(lista_com_n)
    return lista_com_n[list.index(lista_com_n,n)+1:]
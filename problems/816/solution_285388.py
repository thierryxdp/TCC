def maiores(lista,n):
    L=lista
    lista_inse=list.append(L,n)
    lista_orde=list.sort(L)
    indece=list.inde(L,n)
    return lista_orde[0:indece]
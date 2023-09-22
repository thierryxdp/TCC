def maiores(lista,n):
    L=lista
    lista_inse=list.append(L,n)
    lista_orde=list.sort(lista_inse)
    indece=list.inde(lista_orde,n)
    return lista_orde[0:indece]
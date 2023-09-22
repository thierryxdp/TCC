def maiores(lista_num, n):
    listan = [n,]
    nova_lista = lista_num + listan
    list.sort(nova_lista)
    ind_n = list.index(nova_lista, n)
    nova_lista1 = lista[ind_n+1:]
    return nova_lista1
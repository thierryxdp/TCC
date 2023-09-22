def maiores(lista_num, n):
    listan = [n,]
    nova_lista = lista_num + listan
    list.sort(nova_lista)
    ind_n = list.index(lista_num, n)
    nova_lista1 = nova_lista[ind_n+1:]
    return nova_lista1
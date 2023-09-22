def insere(lista_numero, n):
    listan = [n,]
    nova_lista = lista_numero + listan
    list.sort(nova_lista)
    ind_n = list.index(nova_lista,n)
    nova_lista1 = nova_lista[ind_n+1:]
    return nova_lista1
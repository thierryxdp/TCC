def maiores(lista_num, n):
    listan = [n,]
    nova_lista = lista_num + listan
    list.sort(nova_lista)
    nova_lista1 = nova_lista[[n+1]:]
    return nova_lista1
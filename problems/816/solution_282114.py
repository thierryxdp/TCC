def maiores(lista_num, n):
    listan = [n,]
    nova_lista = lista_num + listan
    nova_lista1 = list.sort(nova_lista)
    nova_lista2 = nova_lista[[n+1]:]
    return nova_lista2
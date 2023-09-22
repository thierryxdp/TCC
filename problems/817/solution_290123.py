def insere(lista, n):
    ordem=lista + [n]
    list.sort(ordem)
    return ordem[(list.index(ordem,n)+1):]
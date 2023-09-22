def insere(lista, n):
    ordem=lista + [n]
    list.sort(ordem)
    notas=ordem[(list.index(ordem,n)+1)]
    return sum(notas)
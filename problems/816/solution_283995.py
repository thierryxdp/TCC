def maiores(lista,n):
    lista = lista + [n]
    if lista == lista + [n]:
        return list.sort(lista)
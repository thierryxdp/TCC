def maiores(lista,n):
    lista[0:0] = [n]
    list.sort(lista)
    maiores = lista[(list.index(lista,n))+1:]
    return maiores
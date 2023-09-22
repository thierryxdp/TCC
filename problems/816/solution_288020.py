def maiores(lista,n):
    sorted(lista, key=int)
    list.sort(lista)
    return [i for i in lista if i > n]
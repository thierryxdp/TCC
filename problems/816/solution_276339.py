def maiores(lista,n):
    list.append(lista,n)
    list.sort(lista)
    p=list.index(lista,n)
    maiores=lista[p+1:]
    return maiores
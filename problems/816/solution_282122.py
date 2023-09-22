def maiores(lista, n):
    list.insert(lista,0,n)
    list.sort(lista)
    nobalist = lista[list.index(lista,n)+1:]
    return nobalist
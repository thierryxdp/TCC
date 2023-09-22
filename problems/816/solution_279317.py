def maiores(lista,n):
    if n in lista:
        list.sort(lista)
        posicao = list.index(n,lista)
        lista1 = lista(posicao+1)
        return lista1
    else:
        list.append(lista,n)
        list.sort(lista)
        posicao = list.index(lista,n)
        lista1 = lista[posicao+1:]
        return lista1
def maiores(lista,n):
    if n in lista:
        list.sort(lista)
        return lista[list.count(lista,n)+list.index(lista,n):-1]
    elif n not in lista:
        nlist=list.append(lista,n)
        list.sort(nlist)
        return nlist[list.index(nlist,n)+1:-1]
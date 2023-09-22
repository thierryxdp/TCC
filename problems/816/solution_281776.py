def maiores(lista,n):
    if n in lista:
        nlist=list.sort(lista)
        return nlist[list.count(nlist,n)+list.index(nlist,n):-1]
    elif n not in lista:
        list.append(lista,n)
        nlist=list.sort(lista)
        return nlist[list.count(nlist,n)+list.index(nlist,n):-1]
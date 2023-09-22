def maiores(listanumeros,n):
    listanumeros.append(n)
    list.sort(listanumeros)
    lista=[list.index(listanumeros,n):]
    return lista
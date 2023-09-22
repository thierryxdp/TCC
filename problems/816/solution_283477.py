def maiores(listanumeros,n):
    listanumeros.append(n)
    list.sort(listanumeros)
    lista=listanumeros[list.index(listanumeros,n):]
    return lista
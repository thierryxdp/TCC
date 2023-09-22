def acima_da_media(listanumeros,n):
    listanumeros.append(n)
    list.sort(listanumeros)
    lista=listanumeros[list.index(listanumeros,n)+1:]
    return lista
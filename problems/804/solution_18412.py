def filtra_pares(tupla):
    '''filtra os numeros pares de uma determinada tupla
    tupla -> tupla'''
	tuple2 = tuple()
    if (tupla[0]%2)==0:
        tuple2 = tuple2 + (t[0],)

    if (tupla[1]%2)==0:
        tuple2 = tuple2 + (t[1],)

    if (tupla[2]%2)==0:
        tuple2 = tuple2 + (t[2],)

    if (tupla[3]%2)==0:
        tuple2 = tuple2 + (t[3],)
        return tuple2
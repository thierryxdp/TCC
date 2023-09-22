def filtra_pares(tupla):
    tuplaPar = ()
    if tupla[0] %2 == 0:
        tuplaPar = tuplaPar + (tupla[0],)
    if tupla[1] %2 == 0:
        tuplaPar = tuplaPar + (tupla[1],)
    if tupla[2] %2 ==0:
        tuplaPar = tuplaPar + (tupla[2],)
    if tupla[3] %2 == 0:
        tuplaPar = tuplaPar + (tupla[3],)
    	return tuplaPar
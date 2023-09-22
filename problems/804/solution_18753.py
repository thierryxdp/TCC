def filtra_pares(tup):
    lista = ()
    if tup[0]%2 == 0:
        lista = lista + (tup[0],)
	if tup[1]%2 == 0:
        lista = lista + (tup[1],)
    if tup[2]%2 == 0:
        lista = lista + (tup[2],)
    if tup[3]%2 == 0:
        lista = lista + (tup[3])
    return lista
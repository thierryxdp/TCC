def filtra_pares(tup):
	filtro=[]
    if tup[0]%2==0:
        filtro.append(tup[0])
    if tup[1]%2==0:
        filtro.append(tup[1])
    if tup[2]%2==0:
        filtro.append(tup[2])
    if tup[3]%2==0:
        filtro.append(tup[3])
    return tuple(filtro)
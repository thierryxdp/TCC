def filtra_pares(tupla):
	t1 = list(tupla)
    if t1[0] % 2 != 0:
    	return t1[0]
    else:
        return t1[1]
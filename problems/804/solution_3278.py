def filtra_pares(tupla):
	t1=()
    if tupla[0] % 2 == 0:
        t1 = t1 + tupla[0:1]
    if tupla[1] % 2 == 0:
    	t1 = t1 + tupla[1:2]
    if tupla[2] % 2 == 0:
        t1 = t1 + tupla[2:3]
	if tupla[3] % 2 == 0:
        t1 = t1 + tupla[3:]
	return t1
def filtra_pares(tupla):
	t1 = list(tupla)
    t2 = []
    if t1[0] % 2 == 0:
        t2.append(t1[0])
   	elif t1[1] % 2 == 0:
        t2.append(t1[1])
    elif t1[2] % 2 == 0:
        t2.append(t1[2])
    elif t1[3] % 2 == 0:
        t2.append(t1[3])
    t3 = tuple(t2)
    return t3
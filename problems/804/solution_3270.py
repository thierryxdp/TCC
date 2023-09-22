def filtra_pares(t):
    t1=tuple()
    
    if t[0]%2 == 0:
        t1 = t1 + t[0:1]
    if t[1]%2 == 0:
        t1 = t1 + t[1:2]
    if t[2]%2 == 0:
        t1 = t1 + t[2:3]
    if t[3]%2 == 0:
        t1 = t1 + t[-1:]
	return t1
def filtra_pares(minha_tupla):
	x = []
    a,b,c,d = minha_tupla
	if (a%2==0):
        x.append(a)
	if b%2==0:
        x.append(b)
    if c%2==0:
        x.append(c)
    if d%2==0:
        x.append(d)
	return tuple(x)
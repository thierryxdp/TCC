def filtra_pares(minha_tupla):
	x = [ ]
    a,b,c,d = minha_tupla
	if (a%2==0):
        x.append(a)
	elif b%2==0:
        x.append(b)
    elif c%2==0:
        x.append(c)
    elif d%2==0:
        x.append(d)
    else:
        return tuple(x)
def filtra_pares(t):
	if t[0]/2==int and t[1]/2==int and t[2]/2==int and t[3]/2==int:
        return t
    elif t[0]/2!=int and t[0]/2==int and t[2]/2==int and t[3]/2==int:
        return t[1:]
    elif t[0]/2!=int and t[0]/2!=int and t[2]/2==int and t[3]/2==int:
		return t[2:]
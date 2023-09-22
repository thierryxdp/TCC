def filtra_pares(a,b,c,d):
	if (a,b,c,d)%2 == 0:
        return (a,b,c,d)
    elif (a,b,c)%2 == 0:
        return (a,b,c)
    elif (a,b)%2 == 0:
        return (a,b)
    else:
        return (a)
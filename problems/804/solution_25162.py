filtra_pares (a,b,c,d):
	y=a,b,c,d
    if a%2==0:
        return y[0]
    elif b%2==0:
        return y[1]
    elif c%2==0:
        return [2]
    elif d%2==0:
        return [3]
    elif b%2==0 and a%2==0:
        return y[0:2]
    elif b%2==0 and a%2==0 and c%2==0:
        return y[0:3]
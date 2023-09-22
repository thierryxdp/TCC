def filtra_pares(a,b,c,d):
    x = []
    if (a%2 == 0):
    	x.append(a)
        if (b%2 == 0):
            x.append(b)
            if (c%2 == 0):
                x.append(c)
                if (d%2 == 0):
                    x.append(d)
                    tuple(x)
                    return x
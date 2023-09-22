filtra_pares (num):
    r=[]
    for n in num:
        if n%2==0:
            r.append (n)
	return tuple (r)
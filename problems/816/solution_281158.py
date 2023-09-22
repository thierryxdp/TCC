def maiores(l,n):
    k=[]
    for x in l:
        if x>n:
            k.append(x)
	k.sort()
	return k
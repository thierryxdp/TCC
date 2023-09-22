def uppCons(f):
    r=""
    i=0
    while i < len(f):
        if f[i] in "bcçdfghjklmnpqrstvwxyz":
            r=r+str.upper(f[i])
        else:
            r=r+f[i]
        i = i+1
	return r
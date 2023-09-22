def uppCons(f):
    r=""
    for e in f:
        if e in "bcçdfghjklmnpqrstvwxyz":
            r=r+str.upper(e)
        else:
            r=r+e
	return r
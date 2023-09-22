def uppCons(f):
    r=""
    for e in f:
        if e in "bcdfghjklmnpqrstvwxyz":
            r=r+str.upper(e)
        else:
            r=r+e
	return r
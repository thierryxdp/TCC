def uppCons(f):
	i = 0
    nf = ''
    while i < len(f):
        if f[i] in 'BCDFGHJKLMNPQRSTVXYWZbcdfghjklmnpqrstvxywz':
        	nf = f + f[i].upper()
    	i = i + 1
    return nf
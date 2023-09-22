def uppCons(f):
	i = 0
    nf = ''
    while proximo < len(f):
        if f[i] not in 'AEIOUaeiou':
        nf = nf + f[i].upper
    	i = i + 1
    return nf
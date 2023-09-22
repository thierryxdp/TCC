def uppCons(f):
	i = 0
    nf = ''
    while i < len(f):
        if f[i] is 'AEIOUaeiou':
        	nf = nf + f[i].upper
    	i = i + 1
    return nf
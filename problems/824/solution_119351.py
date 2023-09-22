def uppCons(f):
	i = 0
    nf = ''
    while i < len(f):
        if f[i] is not 'AEIOUaeiou':
        	nf = nf + f[i]
    	i = i + 1
    return nf
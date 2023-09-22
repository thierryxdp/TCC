def lingua_p(f):
	nf = ''
    vogais = 'aeiouAEIOU'
    for i in f:
    	if f in vogais:
        	nf = nf + (f[i] + ('p') + f[i])      
    return nf
def uppCons(f):
	i = 0
    nf = ''
    while i < len(f):
        if f[i] not in 'AEIOUaeiouÃÁÉÍÕÓÚÀÈÌÒÙãáéíõóú':
        	nf = nf + f[i].upper()
        else:
            nf = nf + f[i]
    	i = i + 1
    return nf
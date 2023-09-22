def uppCons(f):
	i = 0
    nf = ''
    consoantes = 'ÇBCDFGHJKLMNPQRSTVXYWZçbcdfghjklmnpqrstvxywz'
    vogais = 'AEIOUaeiouÃÁÉÍÕÓÚÀÈÌÒÙãáéíõóú'
    while i < len(f):
        if f[i] in consoantes:
        	nf = nf + f[i].upper()
        else:
            nf = nf + f[i]
    	i = i + 1
    return nf
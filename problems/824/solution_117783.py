def uppCons(frase):
    ''' '''
    indice=0
    
    while indice < len(frase):
        if frase[indice] in 'BCDFGHJKLMNPQRSTUVWXYZbcdfghjklmnpqrstvwxyz':
            frase.upper('b')
		indice+=1
	return frase
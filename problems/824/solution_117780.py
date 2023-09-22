def uppCons(frase):
    ''' '''
    indice=0
    
    while indice < len(frase):
        if frase[indice] in 'BCDFGHJKLMNPQRSTUVWXYZbcdfghjklmnpqrstvwxyz':
            frase.upper('B')
		indice+=1
	return
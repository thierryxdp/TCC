def uppCons(frase):
    ''' '''
    indice=0
    
    while indice < len(frase):
        if frase[indice] in 'BCDFGHJKLMNPQRSTUVWXYZbcdfghjklmnpqrstvwxyz':
            frase[indice].upper()
		indice+=1
	return frase
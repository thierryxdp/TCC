def uppCons(frase):
    ''' '''
    indice=0
    
    while indice < len(frase):
        if frase[indice] in 'BCDFGHJKLMNPQRSTUVWXYZbcdfghjklmnpqrstvwxyz':
            maiuscula=frase[indice].upper()
		indice+=1
	return maiuscula
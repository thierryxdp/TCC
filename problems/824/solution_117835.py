def uppCons(frase):
    ''' '''
    indice=0
	while indice < len(frase):
    	if frase[indice] in 'bcdfghjklmnpqrstvwxyz':
    		frase = str.upper(frase[indice])
        	frase=frase.replace(frase[indice],frase) 
        indice+=1
    return frase
def uppCons (frase):
    indice = 0
    frase1 = ''
    while indice < len (frase):
        if frase [indice] in 'bcçdfghjklmnpqrstvwxyz': 
			frase1 += str.upper(frase[indice])  
    	else:
            frase1 += frase[indice]
        indice += 1
        
	return frase1
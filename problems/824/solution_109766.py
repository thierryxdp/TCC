def uppCons (frase):
    indice = 0
    while indice < len (frase):
        if frase [indice] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            
		indice += 1                    
	return str.upper(frase[indice])
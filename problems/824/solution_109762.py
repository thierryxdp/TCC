def uppCons (frase):
    indice = 0
    while indice < len (frase):
        if frase [indice] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            str.upper(frase, indice)
		indice += 1                    
	return frase
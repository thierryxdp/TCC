def uppCons(frase):
    vogais = 'aeiou'
	for letra in frase:
    	if letra in vogais:
        	return(letra.upper())
    	else:
        	return(letra)
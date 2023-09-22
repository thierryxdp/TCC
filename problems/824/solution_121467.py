def uppCons(frase):
    vogais = 'aeiou'
	for letra in frase:
    	while letra in vogais:
        	return(letra.upper())
    	else:
        	return(letra)
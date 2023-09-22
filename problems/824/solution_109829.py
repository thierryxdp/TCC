def uppCons(frase):
	listafrase=list(frase)
	for letra in listafrase:
		if letra.lower() in ['a','e','i','o','u']:
			listafrase[listafrase.index(letra)]=letra.upper()
		else:
			continue
	return(''.join(listafrase))
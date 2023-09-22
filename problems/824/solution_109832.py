def uppCons(frase):
	listafrase=list(frase)
	for letra in listafrase:
		if letra.lower() not in ['a','e','i','o','u','ã','â','é','ó','ô','í','ú']:
			listafrase[listafrase.index(letra)]=letra.upper()
		else:
			continue
	return(''.join(listafrase))
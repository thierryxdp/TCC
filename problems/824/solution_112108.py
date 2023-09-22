def uppCons(frase):
	a=len(frase)
	vogais="aeiouAEIOUãáéíóú"
	map(i,a):
		if frase[i] not in vogais:
			frase=list(frase)
			frase[i]=str.upper(frase[i])
			frase=str.join("",frase)
	return frase
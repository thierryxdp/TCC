def uppCons(frase):
	a=len(frase)
	vogais="aeiouAEIOUãéúí"
	for i in range(a):
		if frase[i] not in vogais:
			frase=list(frase)
			frase[i]=str.upper(frase[i])
			frase=str.join("",frase)
	return frase
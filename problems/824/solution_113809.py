def uppCons(frase):
	"""transforma todas as consoantes de uma frase em maiuscula;str->str"""
	i=0
	while i<len(frase):
		str.upper(frase)
		if frase[i]in'AEIOU':
			str.lower(frase[i])
		i+=1
	return frase
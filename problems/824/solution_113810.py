def uppCons(frase):
	"""transforma todas as consoantes de uma frase em maiuscula;str->str"""
	i=0
    nova=''
	while i<len(frase):
		nova=str.upper(frase)
		if frase[i]in'AEIOU':
			nova=str.lower(frase[i])
		i+=1
	return nova
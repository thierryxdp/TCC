def uppCons(frase):
	"""transforma todas as consoantes de uma frase em maiuscula;str->str"""
	i=0
	while i<len(frase):
		if frase[i]in'cçbdfghjklmnpqrstvwxyz':
			frase=str.replace(frase,frase[i],str.upper(frase[i]),i)
		i+=1
	return frase
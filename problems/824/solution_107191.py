def uppCons(frase):
	"""Função que recebe uma frase e retorna esta com todas suas consoantes maiúsculas.
	string -> string"""
	consoantes='qQwWrRtTyYpPsSdDfFgGhHjJkKlLzZxXcCvVbBnNmM'
	i=0
	frase=list(frase)
	retorno=''
	while i<len(frase):
		if frase[i] in consoantes:
			frase[i]=frase[i].upper()
		i=i+1
	return retorno.join(frase)
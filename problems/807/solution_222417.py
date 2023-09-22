def conta_frases(texto):
	"""conta o numero de frases dentro de um texto.
entra texto; str->int"""
	texto=str.replace(texto,'...','#')
	texto=str.replace(texto,'!','#')
	texto=str.replace(texto,'.','#')
	texto=str.replace(texto,'?','#')
	frases=str.count(texto,'#')
	if frases>=1:
		return frases
	else:
		return 0
def quant_palavras(frase):
	"""conta o numero de palavras de uma frase.
entra frase;str->int"""
	frase=str.replace(str.strip(frase),' ','#')
	if str.count(frase,'#')>=1:
		palavras=2+(str.count(frase,'#')-1)
		return palavras
	if frase=='':
		return 0
	else:
		return 1
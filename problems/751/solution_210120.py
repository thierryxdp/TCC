def quant_palavras(frase):
	'''Esta função conta as palavras de uma frase
	string -> int'''
	
    frase = str.strip(frase,'')
    frase_dividida = str.split(frase,'')
    qtd = len (frase_dividida)
    return qtd
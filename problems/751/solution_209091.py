def quant_palavras(frase):
	''' 
    	Função que recebe uma frase e retorna a
		quantidade de palavras que há nela:
    	str->int
	'''
    palavras = str.split(frase) 
    return len(palavras)
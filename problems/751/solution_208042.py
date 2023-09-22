def quant_palavras(frase):
    '''funcao que dada uma frase retorna o numero de palavras da frase.
    frase dada (str) --> número de palavras (int)'''
	frase = "frase com espaço"
	frase = frase.strip()
	frase = frase.split(sep=' ')
	return len(frase)
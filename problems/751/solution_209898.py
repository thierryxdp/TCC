def quant_palavras(frase):
	'''Função que retorna o número de palavras de uma frase
    str -> int'''
    nova=str.strip(frase)
    substrings=str.split(nova,' ')
    return len(substrings)
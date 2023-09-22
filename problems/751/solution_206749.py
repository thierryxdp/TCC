def quant_palavras(frase):
    """Esta função retorna o número de palavras dado uma frase inserida
	str -> int"""

    palavras= str.strip(frase,' ')
    
    return len(palavras)
def quant_palavras(frase):
    """Função que retorna o número de palavras de uma frase
    	str -> int """
    x=str.strip(frase)
    y=str.split(x)
    return len(y)
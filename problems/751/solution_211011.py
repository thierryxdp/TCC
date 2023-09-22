def quant_palavras(frase):
    """
    	Recebe uma frase e retorna a quantidade de palavras
        contidas na frase.
        str --> int
    """
    fraseRepartida = str.split(frase, " ")
    return len(fraseRepartida)
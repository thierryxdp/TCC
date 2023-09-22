def quant_palavras(frase):
    """Recebe uma frase e devolve a quantidade de palavras nela;
    	str -> num"""
    str.strip(frase)
    fraselista=str.split(frase,' ')
    qtd=len(fraselista)
    return qtd
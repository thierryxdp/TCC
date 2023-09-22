def quant_palavras(frase):
    """Conta a quantidade de pavras em uma frase.
    	Str-->int"""
    partes_frase = (str.split(frase, ' '))
    return len(partes_frase)
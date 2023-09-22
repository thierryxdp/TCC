def quant_palavras(frase):
    """Retorna o número de palavras da frase.
    string->string"""
    x=str.split(frase)
    x=list.remove(x,' ')
    return len(x)
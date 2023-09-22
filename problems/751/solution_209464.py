def quant_palavras(frase):
    """retorna o número de palavras em uma frase. (str->int)"""
    palavras = str.split(frase," ")
    return len(palavras)
def quant_palavras(frase):
    """Retorna o número de palavras da frase.
    string->string"""
    return len(frase)-(str.count(frase,' '))
def quant_palavras(frase):
    """Retorna o número de palavras da frase.
    string->string"""
    x=str.split(frase)
    return len(frase)-(list.count(frase,' '))
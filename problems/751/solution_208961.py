def quant_palavras(frase):
    """dada a frase, retorna o número de palavras da frase.
str->int"""
    lista_palavras= str.split(frase)
    return len(lista_palavras)
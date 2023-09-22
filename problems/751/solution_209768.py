def quant_palavras(frase):
    ''' Esta função calcula a quantidade de palavras em uma frase.
    str -> int'''
    palavras_separadas = str.split(frase)
    return len(palavras_separadas)
def quant_palavras(frase):
    '''Função retorna a quantidade de palavras de uma frase
    str -> int'''
    palavras = str.split(frase)
    numero_palavras = len(palavras)
    return numero_palavras
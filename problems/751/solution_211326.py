def quant_palavras(frase):
    '''Funcao para receber uma string e contar o numero de palavras
    str -> int'''
    numero_palavras = str.split(frase)
    return len(numero_palavras)
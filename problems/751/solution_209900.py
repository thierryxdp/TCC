def quant_palavras(frase):
    '''função que dada uma frase retorna o número de palavras da frase
    str -> int
    '''
    palavras = str.split(frase)
    quantidade = len(palavras)
    return quantidade
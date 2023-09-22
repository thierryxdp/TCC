def quant_palavras(frase):
    '''
    Função conta quantas palavras tem na frase inserida.
    str -> int
    '''
    lista = str.split(frase)
    quant = len(lista)
    return quant
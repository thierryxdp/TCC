def quant_palavras (frase):
    '''Função que conta quantas palavras tem uma frase'''
    #str -> int
    frase = str.split(frase)
    return len(frase)
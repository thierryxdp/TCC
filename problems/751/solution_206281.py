def quant_palavras(frase):
    '''Funcao que recebe uma string e retorna o numero de palavras da frase desconsiderando os espacos;
    str -> int'''
    frase = frase.split()
    return len(frase)
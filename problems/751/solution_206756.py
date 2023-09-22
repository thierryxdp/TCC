def quant_palavras(frase):
    '''Função que recebe uma frase e retorna o número de palavras da frase;
    str -> int'''
    palavras = str.split(frase)
    return len(palavras)
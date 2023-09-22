def quant_palavras(frase):
    '''Funçao que recebe uma frase e retorna o numero de palavras contidas nela (str -> int)'''
    return str.count(str.strip(frase), ' ') + 1
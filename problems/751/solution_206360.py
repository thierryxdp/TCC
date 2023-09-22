def numPalavras(f):
    '''Funçao que recebe uma frase e retorna o numero de palavras contidas nela (str -> int)'''
    return str.count(str.strip(f), ' ') + 1
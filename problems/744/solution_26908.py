import math
def hashtag (s):
    '''Retorna a string inserida "s" porém com o caractere "#" inserido no início, no meio e no final da dela;
    str -> str'''
    tamanho = len(s)
    metade = math.floor(tamanho/2)
    parte1 = '#' + s[:metade]
    parte2 = '#' + s[metade:] + '#'
    return parte1 + parte2
import math
def hashtag(s):
    '''Função que retorna uma string e insere o caractere '#'
    no início, no meio e no final dela.
    s=str->str'''
    x = math.floor(len(s)/2)
    return '#' + s[0:x] + '#' + s[x:] + '#'
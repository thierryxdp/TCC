import math
def hashtag(s):
    '''calcule e retorne uma função que receba uma string e insira o caractere '#' no início, no meio e no final dela. str-->tupla.'''
    funcao = len (s)
    if funcao == 0:
        return '###'
    else:
        s = s[0:(math.floor(funcao/2))] + '#' + s[(math.floor(funcao/2)):-1] + s[-1]
        s = '#' + s 
        s = s + '#'
        return s
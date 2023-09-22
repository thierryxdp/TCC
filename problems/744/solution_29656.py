from math import *

def hashtag(s):
    '''
    Dado uma string adiciona # na mesmma
    
    Uso:
    hashtag(s):
    
    Entrada:
    - s (str, obrigatória): variavél 1
    
    Saída:
    - Uma string adaptada com # no início, meio e fim
    '''
    return '#' + s[0:len(s)//2]+ '#' +s[len(s)//2:] + '#'
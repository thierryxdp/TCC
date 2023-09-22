# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str

import math

def hashtag(s):
    '''Inserir palavra entre aspas.
    Inserir palavra entre aspas.
    str-> str '''
    
    return '#' + s[0:math.floor(len(s)/2)] + '#' + s[math.floor(len(s)/2):len(s)] + '#'
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str

import math

def hashtag(s):
    
    return '#' + s[1:math.floor(len(s)/2)] + '#' + s[math.floor(len(s)/2):len(s)] + '#'
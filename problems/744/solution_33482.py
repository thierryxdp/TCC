# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str

import math
def hashtag(s):
    nome = s
    return '#' + nome[0:math.floor(len(nome)/2)] + '#' + nome[math.floor(len(nome)/2):] + '#'
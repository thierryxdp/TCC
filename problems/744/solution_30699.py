# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
from math import floor
def hashtag(s):
    meioFrase = floor(len(s) / 2)
    return '#'.join(s, meioFrase) + '#'
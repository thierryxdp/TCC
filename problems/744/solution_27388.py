# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
from math import *
def hashtag(s):
    c=len(s)
    return '#'+s[0:floor(c/2)]+'#'+s[floor(c/2):c]+'#'
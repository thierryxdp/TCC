# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
from math import flor
def hashtag(s):
    return '#'+s[0:int(floor(len(s)/2))]+'#'+s[int(floor((len(s)/2))):-1]+s[-1]+'#'
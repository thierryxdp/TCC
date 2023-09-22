# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
from math import ceil
def hashtag(s):
    return '#'+s[:ceil(len(s)/2)]+'#'+s[ceil(len(s)/2+1)]+'#'
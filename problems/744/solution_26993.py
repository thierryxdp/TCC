# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
from math import floor
from math import ceil
def hashtag(s):
    '''funcao que adiciona uma # no inicio, no meio e no final de uma string
    str->str'''
    x=int(floor(len(s)/2))
    y=len(s)
    a=s[0:x]
    b=s[x:y]
    return '#'+a+'#'+b+'#'
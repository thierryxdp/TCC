import math
def hashtag(s):
    '''Retorna uma funcao que insere o caractere # no inicio, no meio e no final dela
    str -> str'''
    medio=len(s)/2
    return '#'+s[0:math.floor(medio)]+'#'+s[math.floor(medio):]+'#'
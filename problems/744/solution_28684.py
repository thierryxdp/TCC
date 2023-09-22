# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    '''Coloca a hashtag no ínicio, no meio e no fim da palavra.
    str -> str'''
    x = math.floor(len(s)/2)
    s1 = '#'+s[:x]+'#'+s[x:]+'#'
    return s1
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    '''essa funcao coloca um # no inicio, meio e fim 
    da string'''
    '''str -> str'''
    if len(s)%2==0:
        y = ((len(s)//2))
        return '#'+s[0:y]+'#'+s[y:]+'#'
    else:
        z = ((len(s)//2)-1)
        return '#'+s[0:z]+'#'+s[z:]+'#'
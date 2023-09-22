# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
from math import *
def hashtag(s):
    '''Recebe uma string s e adiciona o caractere # no começo, meio e
    fim da string'''
    '''str->str'''
    q=len(s)
    '''q representa a quantidade de caracteres em s'''
    m=floor(q/2)
    '''m representa o índice do caractere do meio de s'''
    return '#'+s[0:m]+'#'+s[m:q]+'#'
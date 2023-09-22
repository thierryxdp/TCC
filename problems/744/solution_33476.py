# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    '''Função que recebe uma string e retorna essa string com o caractere '#' no início, meio e fim dela
    str -> str'''
    return '#'+s[0:math.ceil((len(s))/2)]+'#'+s[math.ceil((len(s))/2):]+'#'
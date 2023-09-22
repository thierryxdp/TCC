# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    '''insere uma # no inicio, meio e final de uma string'''
    x = s[0:math.floor(len(s)/2)]
    y = s[math.floor(len(s)/2):len(s)]
    
    return '#' + x + '#' + y + '#'
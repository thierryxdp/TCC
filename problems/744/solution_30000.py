# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    '''retornar a string separada por hashtags no inicio, meio e fim'''
    if len(s) <= 4:
        return ('#' + s[0:1] + '#' + s[2:3] + '#')
    
    if len(s) = 7 or len(s) = 8:
        return ('#' + s[0:3] + '#' + s[4:7] + '#')
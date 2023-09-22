# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    '''retornar a string separada por hashtags no inicio, meio e fim'''
    if len(s) <= 9:
        return ('#' + s[1:4] + '#' + s[4:9] + '#')
    
    if len(s) <= 8:
        return ('#' + s[1:4] + '#' + s[4:8] + '#')
    
    if len(s) <= 7:
        return ('#' + s[1:3] + '#' + s[4:7] + '#')
    
    if len(s) <= 6:
        return ('#' + s[0:3] + '#' + s[3:6] + '#')
    
    if len(s) <= 5:
        return ('#' + s[0:2] + '#' + s[3:5] + '#')
    
    if len(s) <= 4:
        return ('#' + s[0:2] + '#' + s[2:4] + '#')
    
    if len(s) <= 3:
        return ('#' + s[0:1] + '#' + s[2:3] + '#')
    
    if len(s) <= 2:
        return ('#' + s[0:1] + '#' + s[1:2] + '#')
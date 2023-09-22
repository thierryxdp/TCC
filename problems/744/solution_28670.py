# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    ''' Adiciona e retorna # no inicio, no meio e no final de uma string s
        str -> str'''
    
    meio_s = math.floor(len(s) / 2)
    
    s_2 = '#' + s[:meio_s] + '#' + s[meio_s:] + '#'
    
    return s_2
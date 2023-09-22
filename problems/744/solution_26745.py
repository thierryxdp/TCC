# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
from math import floor

def hashtag(s):
    '''Recebe uma string e retorna a mesma com um # no início, meio
    e final da mesma.
    string -> string'''
    
    numero = floor(len(s)/2)
    string_i = s[:numero]
    string_f = s[numero:]
    htg = '#'
    
    return htg + string_i + htg + string_f + htg
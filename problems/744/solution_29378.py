# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    y = len (s)
    c = y/2
    b = math.floor(c)
    return '#'+ s[0:b] + '#' + s[b:y] + '#'
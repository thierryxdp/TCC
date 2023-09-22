# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    parte_1 = s[0:math.floor(len(s)/2)]
    parte_2 = s[math.floor(len(s)/2):len(s)]
    return '#' + parte_1 + '#' + parte_2 + '#'
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
from math import floor
def hashtag(s):
    """Essa função recebe uma string e insere '#' no ínicio, no meio e no final dela."""    
    mid = floor(len(s) /2)
    return '#' + s[0:mid] + '#' + s[mid:] + '#'
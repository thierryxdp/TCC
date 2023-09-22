# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    """retornara a mesma string porém com '#' no início, meio e fim dela
    str -> str""""
    b= len(s)
    a= math.floor(b/2)
    return '#'+s[0:a]+'#'+s[a:b]+'#'
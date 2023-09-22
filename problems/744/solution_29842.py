# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    b= len(s)
    a= math.floor(s/2)
    return '#'+s[0:a]+'#'+s[a:b]+'#'
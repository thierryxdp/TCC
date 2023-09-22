# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    p1 = s[0:math.floor(len(s)/2)]
    p2 = s[math.floor(len(s)/2):len(s)]
    
    return '#'+p1+'#'+p2+'#'
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    metade=math.ceil(s/2)
    return '#'+s[:metade]+'#'s[metade:]+'#'
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
import math
def hashtag(s):
    meio=math.floor(len(s)/2)
    return '#'+s[:meio]+'#'+s[meio:]+'#'
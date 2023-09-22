# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    import math
    return '#'+s[:(math.floor(len(s)/2))]+'#'+s[(math.floor(len(s)/2)):]+'#'
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    import math
    m=math.floor(len(5)/2)
    return '#'+s[0:m:]+'#'+s[m::]+'#'
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    import math
    meio = len (s)/2
    meio = math.floor (meio)
    parte1 = s[0:meio]
    parte2 = s[meio:]
    return '#'+parte1+'#'+parte2+'#'
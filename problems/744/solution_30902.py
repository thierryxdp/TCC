# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    meio =math.ceil(len(s)/2)
    return '#' + s[:meio-1] + '#' + s[meio:] +'#'
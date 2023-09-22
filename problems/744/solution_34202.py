# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    sl=len(s)
    return "#" + (s)[0:(sl/2)] + "#" + (s)[(sl/2):sl] + "#"
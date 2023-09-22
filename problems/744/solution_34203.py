# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    sl=len(s)
    return "#" + (s)[0:(math.floor (sl/2))] + "#" + (s)[(math.floor(sl/2)):sl] + "#"
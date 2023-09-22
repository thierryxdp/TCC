# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    meio = len(s)/2
    meio = int(math.floor(meio))
    M = "#" + s[:meio] + "#" + s[meio:] + "#"
    return M
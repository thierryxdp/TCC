import math
def insertChar(s):
    meio = len (s)/2
    meio = int(math.floor(meio))
    mystring	= '#'+s[:meio] + s[meio:] +'#'
    return mystring# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
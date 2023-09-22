# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(x):
    a=math.floor(len(x)/2)
    dividir1=x[:a]
    dividir2=x[a:]
    soma= '#'+dividir1+'#'+dividir2+'#'
    return somas
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
from math import floor 
def hashtag(s):
    y=floor(len(s)/2)
    sub1=s[0:(y+1)]
    sub2=s[(y+1):]
    return '#'+sub1+'#'+sub2+'#'
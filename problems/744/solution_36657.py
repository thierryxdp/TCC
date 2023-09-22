# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
from math import floor 
def hashtag(s):
    y=floor(len(s)/2)
    sub1=s[0:y]
    sub2=s[y:]
    return '#'+sub1+'#'+sub2+'#'
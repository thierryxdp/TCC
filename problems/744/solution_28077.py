# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
from math import floor
def hashtag(s):
    ''' funcao insere uma hashtag no comeco meio e fim da string, str->str'''
    if s == '':
        return '###'
    else:
    	return '#'+s[0:int(floor(len(s)/2))]+'#'+s[int(floor((len(s)/2))):-1]+s[-1]+'#'
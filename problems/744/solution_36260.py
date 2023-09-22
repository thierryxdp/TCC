# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    '''retorna uma string com # no começo 
    no meio e no fim, dado uma string'''
    return "#"+s[ :(math.floor(len(s)/2))]+"#"+s[(round(len(s)/2)): ]+"#"
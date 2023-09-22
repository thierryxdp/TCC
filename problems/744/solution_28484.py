# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    '''funcao que recebe uma string e insere '#' no inicio, no meio e no final;str-->str'''
    x=len(s)
    return '#' + s[:math.floor(x/2)]+'#'+s[math.floor(x/2):]+'#'
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    '''A funcao recebe uma uma string e insere
       o # no ininicio, no meio e no final da 
       strin;
       str -> str'''
    return '#'+s[:math.floor(len(s)/2)]
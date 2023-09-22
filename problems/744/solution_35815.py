# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    '''retorna a string s com '#' no início, meio e final dela'''
    meio=math.floor(len(s)/2)
    return '#'+s[:meio]+'#'+s[meio:]+'#'
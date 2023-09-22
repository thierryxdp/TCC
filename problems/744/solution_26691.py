import math
def hashtag(s):
    '''retorna uma string com "#" no início, meio e final do string de entrada;
    str -> str'''
    meio=math.floor(len(s)/2)
    return '#'+s[:meio]+'#'+s[meio:]+'#'
import math
def hashtag(s):
    '''função que retorna str com # no inicio, meio e fim
    str-> str'''
    return '#'+s[0:(math.floor(len(s)/2))]+'#'+s[(math.ceil(len(s)/2)):]+'#'
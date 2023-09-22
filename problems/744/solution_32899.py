def hashtag(s):
    '''função que retorna str com # no inicio, meio e fim
    str-> str'''
    import math
    return '#'+s[0:(ceil(len(s)/2))]+'#'+s[(round(len(s)/2)):]+'#'
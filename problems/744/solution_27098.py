def hashtag(s):
    '''insere uma hashtag no início, meio e fim fe uma string'''
    import math
    return '#'+s[0:math.floor((len(s)/2))+'#'+s[math.floor((len(s)/2)):]+'#'
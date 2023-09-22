import math
def hashtag(s):
    '''string->string'''
    return '#'+s[0:((len(s)//2)+1)]+'#'+s[(len(s)//2):]+'#'
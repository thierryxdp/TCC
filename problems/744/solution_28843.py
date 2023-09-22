import math
def hashtag(s):
    '''string->string'''
    return '#'+s[0:math.ceil(len(s)//2)]+'#'+s[math.ceil(len(s)/2):]+'#'
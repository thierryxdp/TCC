import math
def hashtag(s):
    """hashtag"""
    x=len(s)%2
    return '#'+s[0:x]+'#'+s[x:]+'#'
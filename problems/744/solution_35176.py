import math
def hashtag(s):
    a=math.floor(len(s)/2)
    return '#'+s[0:a]+'#'+s[a:]+'#'
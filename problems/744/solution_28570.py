def hashtag(s):
     """funçao que comoca uma hashtag no inicio, meio e
     no final da str"""
    import math
    m=math.floor(len(s)/2)
    return '#'+s[0:m:]+'#'+s[m::]+'#'
def hashtag(s):
    a=len(s)
    b=a//2
    return '#'+str(s[0:b])+'#'+str(s[b:])+'#'
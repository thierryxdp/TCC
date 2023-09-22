def hashtag(s):
    a=int((len(s))/2)
    b= '#'+s[:a]+'#'+s[a:]+'#'
    return b
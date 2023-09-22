def hashtag(s):
    """retorna uma função que ao receber"""
    metade=(len(s))/2
    return '#'+s[0:metade:1]+'#'+s[metade:]+'#'
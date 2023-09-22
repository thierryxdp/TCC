def hashtag(s):
    """função que retorna a str de entrada com simbolo "#" em seu início, meio e fim. str->str"""
    r=len(str(s))
    return '#'+str(s)[0:r/2]+'#'+str(s)[r/2: ]+'#'
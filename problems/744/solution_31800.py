def hashtag(s):
    """funçao que recebe uma string e adiciona # no inicio
    meio e fim de string, exceto se a string for unitária pois
    nao possui meio
    str -> str"""
    a=len(s)//2

    if len(s)>1:
        return '#'+s[0:a]+'#'+s[a:]+'#'
    else:
        return '#'+s+'#'
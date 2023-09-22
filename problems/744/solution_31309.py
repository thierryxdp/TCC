def hashtag(s):
    """Insere o caractere ‘#’ no inicio, meio e final de uma string.
    str->str"""
    x=int(len(s)/2)
    return '#'+s[0:x]+'#'+s[x:]+'#'
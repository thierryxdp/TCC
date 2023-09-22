def hashtag(s):
    """Função que retorna a string dividida em duas partes com # entre elas
       string->string"""
    len(s)
    if len(s)>=5:
        return '#'+s[0:2]+'#'+s[2:]+'#'
    else:
        return '#'+s[0:4]+'#'+s[4:]+'#'
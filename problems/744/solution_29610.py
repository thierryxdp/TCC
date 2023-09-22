def hashtag(s):
    """Recebe uma string e retorna uma string com o caractere '#' inserido no início, meio e final dela. "string-->Sttring. """
    a= int(len(s)/2)
    b= int(len(s))
    return '#'+s[0:a]+'#'+s[a:b]+'#'
def hashtag(s):
    """Recebe uma string e retorna uma string com o caractere '#' inserido no início, meio e final dela. "string-->Sttring. """
    a= len(s)/2
    b= len(s)
    return '#'+s[1:a]+'#'+s[a:b]+'#'
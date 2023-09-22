def hashtag(s):
    """Retorna a string de entrada acrescida de # no seu início, meio e fim;
       str->str"""
    return '#'+s[:len(s)//2]+'#'+s[len(s)//2:]+'#'
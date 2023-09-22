def hashtag (s):
    """dada uma string como parametro, retorna essa string com hastag no inicio, meio e fim;
    str->str"""
    metade1= s[0:len(s)//2]
    metade2= s[len(s)//2:]
    return '#'+metade1+'#'+metade2+'#'
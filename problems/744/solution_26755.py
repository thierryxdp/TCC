def hashtag(s):
    """insere o # no inicio, meio e fim de uma string
    string -> string"""
    metade=len(s)//2
    c='#'+s[:metade]+'#'+s[metade:]+'#'
    return c
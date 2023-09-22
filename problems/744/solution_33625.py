def hashtag(s):
    """Funcao que retorna um caractece # no inicio, meio e fim de uma string.
    str->str"""
    s=str(s)
    a=lens(s)
    return "#" + s[0:a//2] + "#" + s[a//2:] + "#"
def inverte(frase):
    a=str.lower(frase)
    b=str.strip(a,'!?/.:;')
    c=reversed(b)
    return c
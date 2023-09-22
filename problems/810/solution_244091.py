def inverte(frase):
    """..."""
    x = frase
    u = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(x, "-", " "), ",", " "), ":", " "), ";", " "), "!", " "), "?", " "), ".", " ")
    y = str.split(str.lower(u))
    a = list(u)
    a.reverse()
    c = ''.join(a)
    return c
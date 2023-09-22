def inverte(frase):
    """..."""
    x = frase
    y = str.split(str.lower(x))
    u = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(y, "-", " "), ",", " "), ":", " "), ";", " "), "!", " "), "?", " "), ".", " ")
    a = list(u)
    a.reverse()
    c = ''.join(a)
    return c
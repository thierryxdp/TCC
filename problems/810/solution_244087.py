def inverte(frase):
    """..."""
    x = frase
    y = str.split(str.lower(x))
    a = list(y)    
    a.reverse()
    c = ''.join(a)
    if "-" or "," or ":" or ";" or "!" or "?" or "." in x:
         return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(c, "-", " "), ",", " "), ":", " "), ";", " "), "!", " "), "?", " "), ".", " ")
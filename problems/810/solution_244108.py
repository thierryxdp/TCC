def inverte(frase):
    """Dada uma frase, retorna outra frase que contém as palavras da entrada ivertidas, sem letras maiusculas e sem a pontuação
    str -> str"""
    x = frase
    u = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(x, "-", " "), ",", " "), ":", " "), ";", " "), "!", " "), "?", " "), ".", " ")
    y = str.split(str.lower(u))
    a = list(y)
    a.reverse( )
    c = ' '.join(a)
    return c
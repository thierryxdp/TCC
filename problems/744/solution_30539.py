def hashtag(a):
    """ Recebe uma string "a" e adiciona caracteres "#" no início,
meio e fim dela.
string -> string
"""
    indice = len(a)//2
    return "#"+a[:indice]+"#"+a[indice:]+"#"
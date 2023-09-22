def uppCons(frase):
    """função que retorna as letras consoantes em maiuscula
    str -> str"""
    i = 0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            str.upper(frase[i])
            i = i + 1
    return frase
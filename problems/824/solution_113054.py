def uppCons(frase):
    """função que retorna as letras consoantes em maiuscula
    str -> str"""
    i = 0
    s = ''
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            s = str.upper(frase) 
        i = i + 1
    return s
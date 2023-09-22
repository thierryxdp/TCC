def uppCons(frase):
    """função que retorna as letras consoantes em maiuscula
    str -> str"""
    s = ''
    i = 0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            s = str.upper(frase[i])           
        i = i + 1    
    return s
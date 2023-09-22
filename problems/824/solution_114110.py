def uppCons(frase):
    """função que retorna as letras consoantes em maiuscula
    str -> str"""
    c = ''
    i = 0
    while i <len(frase):
        l = frase[i]
        if (frase[i]) in 'bcdfghjklmnpqrstvxwyzç':
            l = str.upper(l)
            c = c + l               
        i += 1
    return c
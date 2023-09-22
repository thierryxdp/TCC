def uppCons(frase):
    """calculo e retorno de uma fuçao que retorne as consoantes em letra maiusculas."""
    f=' '
    x=frase
    if x in 'bcdfghjklmnpqrstvxwyz':
        f+= x.upper()
    else:
        f+=x
    return f
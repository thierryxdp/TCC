def uppCons (frase->str):
    """receba como entrada uma frase e retorne a frase com todas as suas 
    consoantes em maiusculas"""
    i = 0
    aux = ''
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            aux += frase[i].upper()
        else:
            aux += frase[i]
        i += 1
    return aux
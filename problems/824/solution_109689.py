def uppCons(frase):
    s = ''
    while caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            s += caractere.upper()
    return s
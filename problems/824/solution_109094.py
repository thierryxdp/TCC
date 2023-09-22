def uppCons(frase):
    s = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            s += caractere.upper()
            s += caractere
    return s
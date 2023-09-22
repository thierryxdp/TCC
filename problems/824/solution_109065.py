def uppCons(frase):
    s = ''
    for letra in frase:
        if letra in 'bcdfghjklmnpqrstvxwyz':
            s += letra.upper()
        else:
            s += letra
    return s
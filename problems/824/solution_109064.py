def uppCons(frase):
    s = ''
    for letra in frase:
        if letra in 'bcdfghjklmnpqrstvxwyz':
            s += caractere.upper()
        else:
            s += caractere
    return s
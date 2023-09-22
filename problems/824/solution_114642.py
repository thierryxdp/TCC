def uppCons(frase):
    s = ''
    i = 0
    caractere = frase[i]
    while i<len(frase):
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            s += caractere.upper()
            i = i+1
        else:
            s += caractere
            i = i+1
    return s
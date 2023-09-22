def uppCons(frase):
    s = ''
    i = 0
    caractere = frase[i]
    while caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            s += caractere.upper() 
        else:
            s += caractere
    return s
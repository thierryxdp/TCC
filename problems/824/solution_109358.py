def uppCons(frase):
    i = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvwxyz':
            i += caractere.upper()
        else:
            i += caractere
    return i
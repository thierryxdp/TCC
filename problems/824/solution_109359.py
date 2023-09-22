def uppCons(frase):
    i = ''
    for caractere in frase:
        if caractere in 'bcçdfghjklmnpqrstvwxyz':
            i += caractere.upper()
        else:
            i += caractere
    return i
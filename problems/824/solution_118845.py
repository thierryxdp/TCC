def uppCons(frase):
    mudado = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            mudado += caractere.upper()
        else:
            mudado += caractere
    return mudado
def uppCons(frase):
    mudado = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyzç':
            mudado += caractere.upper()
        else:
            mudado += caractere
    return mudado
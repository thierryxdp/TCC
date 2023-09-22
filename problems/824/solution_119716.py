def uppCons(frase):
    frase2 = ''
    for letra in frase:
        if letra in 'bcdfghjklmnpqrstvwxyz':
            frase2 += letra.upper()
        else:
            frase2 += letra
            return frase2
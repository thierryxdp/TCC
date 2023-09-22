def uppCons(frase):
    frase2 = ''
    for letra in frase:
        if letra in 'bcdfghjklmnpqrstvwxyz':
            frase2 += letra.upper()
            return frase2
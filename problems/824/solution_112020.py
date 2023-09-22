def uppCons(frase):
    s = ''
    for letra in frase:
        if letra in 'bcdfghjklmnpqrstvxwyzç':
            s += letra.upper()
        else:
            s += letra
    return s
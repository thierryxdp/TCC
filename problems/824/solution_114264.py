def uppCons(frase):
    nova = ''
    for letra in frase:
        if letra in 'bcdfghjklmnpqrstvxyzç':
            nova += letra.upper()
        else:
            nova += letra
    return nova
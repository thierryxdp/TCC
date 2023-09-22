def uppCons(frase):
    novafrase = ''
    for i in frase:
        if i in 'bcdfghjklmnpqrstvxyz':
            novafrase += i
        else:
            novafrase += i.upper()
    return novafrase
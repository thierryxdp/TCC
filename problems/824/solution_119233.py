def uppCons(frase):
    novafrase = ''
    for i in frase:
        if i not in 'bcdfghjklmnpqrstvxyz':
            novafrase += i.upper()
        else:
            novafrase += i
    return novafrase
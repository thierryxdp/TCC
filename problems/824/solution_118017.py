def uppCons(frase):
    frase_nova = ''
    i = 0
    while i < len(frase):
        letra = frase[i]
        if letra.lower() in 'bcdfghjklmnpqrstvçz':
            letra = letra.upper()
        frase_nova += letra
        i += 1
    return frase_nova
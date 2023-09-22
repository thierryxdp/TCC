def uppCons(frase):
    i = 0
    frase_nova = ' '
    while i < len(frase):
        if i in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVW':
           frase_nova += frase[i].upper()
        else:
            frase_nova += frase[i]
        i += 1
    return frase_nova
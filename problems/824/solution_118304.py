def uppCons(frase):
    i = 0
    frase_final = str()
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            frase[i].upper += frase_final
        else:
            frase[i].lower += frase_final
    i += 1
    return frase_final
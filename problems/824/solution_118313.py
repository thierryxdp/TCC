def uppCons(frase):
    i = 0
    frase_final = ''
    while i < len(frase):
        if frase[i] in 'bcçdfghjklmnpqrstvwxyz':
            str.upper(frase[i]) += frase_final
        else:
            frase[i] += frase_final
    i += 1
    return frase_final
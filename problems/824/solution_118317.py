def uppCons(frase):
    i = 0
    frase_final = ''
    while i < len(frase):
        if frase[i] in 'bcçdfghjklmnpqrstvwxyz':
            frase_final = frase_final + str.upper(frase[i])
        else:
            frase_final = frase_final + frase[i]
    i += 1
    return frase_final
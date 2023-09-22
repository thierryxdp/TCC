def uppCons(frase):
    i = 0
    frase_final = ''
    while i < len(frase):
        if frase[i] in 'bcçdfghjklmnpqrstvwxyz':
            frase_final += str.upper(frase[i])
            i += 1
        else:
            frase[i] += frase_final
    		i += 1
    return frase_final
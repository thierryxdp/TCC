def uppCons(frase):
    frase_final = ''
    i=0
    while i < len(frase):
        if frase[i] not in 'aeiouAEIOU':
            frase_final += frase[i].upper()
        else:
            frase_final += frase[i]
    return frase_final
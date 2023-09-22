def uppCons(frase):
    frase_tratada = ''
    i=0
    while i<len(frase):
        caractere = frase[i]
        if caractere in 'abcdfghjklmnpqrstwxyz':
            caractere = str.upper(caractere)
        frase_tratada += caractere
        i += 1
    return frase_tratada
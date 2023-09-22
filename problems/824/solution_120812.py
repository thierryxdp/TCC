def uppCons(frase):
    frase_tratada = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvwxyz':
            caractere = str.upper(caractere)
    frase_tratada = frase_tratada + caractere
    
    return frase_tratada
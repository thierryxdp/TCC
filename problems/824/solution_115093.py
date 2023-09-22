def uppCons(frase):
    s = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyçz':
            s += frase.upper()
        else:
            s += caractere
    return frase
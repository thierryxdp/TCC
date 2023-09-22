def uppCons(frase):
    s = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyçz':
            s += caractere.upper()
        if caractere not in 'bcdfghjklmnpqrstvxwyçz':
            s += caractere.lower()
    return frase
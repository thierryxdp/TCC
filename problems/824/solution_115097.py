def uppCons(frase):
    s = ''
    for caractere in frase:
        if caractere not in 'bcdfghjklmnpqrstvxwyçz':
            s += caractere.upper()
        else:
            s += caractere.lower()
    return caractere
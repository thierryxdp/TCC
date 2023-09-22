def uppCons(frase):
    s = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyçz':
            s += caractere.upper()
        else:
            s += caractere
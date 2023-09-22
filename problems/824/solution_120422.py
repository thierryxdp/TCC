def uppCons(frase):
    s = ''
    for e in frase:
        if e in 'bcçdfghjklmnpqrstvxwyz':
            s += e.upper()
        else: 
            s += e
    return s
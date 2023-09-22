def uppCons(frase):
    s = ''
    for e in frase:
        if e in 'bcdfghjklmnpqrstvxwyz':
            s += e.upper()
        else: 
            s += e
    return s

return(uppCons('abcdef'))
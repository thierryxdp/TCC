def uppCons(frase):
    s = ''
    próximo=0
    while proximo<len(frase):
        if frase[proximo] in 'bcdfghjklmnpqrstvxwyz':
            s += frase[proximo].upper()
    return s
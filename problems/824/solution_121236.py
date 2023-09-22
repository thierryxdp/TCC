def uppCons(frase):
    s = ''
    i =0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpçqrstvxwyz':
            s += frase[i].upper()
        else:
            s +=frase[i]
        i += 1
    return s
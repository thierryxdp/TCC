def uppCons(frase):
    conso = ''
    x = 0
    while x == len(frase)-1:
        if frase[x] in 'bcdfghjklmnpqrstvxywz':
            str.replace(frase, frase[x], str.upper(frase[x]))
        conso = conso + str.replace(frase, frase[x], str.upper(frase[x]))
        x = x +1
    return conso
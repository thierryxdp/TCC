def uppCons(frase):
    conso = ''
    x = 0
    while x < len(frase):
        if frase[x] in 'bcdfghjklmnpqrstvxywz':
            conso = conso + str.replace(frase, frase[x], str.upper(frase[x]))
        x = x +1
    return str.replace(frase, frase[x], conso)
def uppCons(frase):
    i=0
    cont = ''
    while i<len(frase):
        if frase[i]in 'bcdfghjklmnpqrstvxwyz':
            str.upper(frase[i])
            cont = cont + frase[i]
        i=i+1
    return frase
def uppCons(frase):
    cm = ''
    for letra in frase:
        if letra in 'bcdfghjklmnpqrstvxwyz':
            cm += letra.upper() 
    return cm
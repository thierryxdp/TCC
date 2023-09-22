def uppCons(frase):
    cm = ''
    for letra in frase:
        if letra in 'bcdfghjklmnpqrstvxwyz':
            cm += letra.upper() 
        else: 
            cm += letra
    return cm
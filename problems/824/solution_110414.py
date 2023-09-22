def uppCons(frase):
    final = ''
    for letra in frase:
        if letra in 'bcdfghjklmnpqrstvxwyz':
            final += letra.upper() 
        else: 
            final += letra
    return final
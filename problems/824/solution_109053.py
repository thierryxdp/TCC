def uppCons(frase):
    f = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            f += caractere.upper() 
        else: 
            f += caractere
    return f
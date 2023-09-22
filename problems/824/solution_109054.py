def uppCons(frase):
    f = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyzç':
            f += caractere.upper() 
        else: 
            f += caractere
    return f
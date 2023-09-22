def uppCons(frase):
    final = ''
    for letra in frase:
        if letra in 'bcdfghjklmnpqrstvxwyz':
            final += caractere.upper() 
        else: 
            final += caractere
    return final